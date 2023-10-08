import os
import requests

# variables
common_name = os.environ['common_name']
ip = os.environ['untrusted_ip']
sent = os.environ['bytes_sent']
received = os.environ['bytes_received']
gotifyurl = ""
gotifytoken = ""
discordurl = ""

# main
if gotifyurl != "":
    resp = requests.post(f'{gotifyurl}/message?token={gotifytoken}', json={
        "title": "Client disconnected from vpn ",
        "message": f"{common_name} {ip} bytes sent: {sent} bytes received: {received}",
        "priority": 10
    })
if discordurl != "":
    resp = requests.post(discordurl, json={
    "embeds": [
        {
            "title": "VPNWATCHDOG",
            "color": 12387853,
            "description": "Client disconnected",
            "fields": [
                {
                    "name": "Client name:",
                    "value": common_name,
                },
                {
                    "name": "IP:",
                    "value": ip,
                },
                {
                    "name": "Bytes sent:",
                    "value": sent,
                },
                {
                    "name": "Bytes received:",
                    "value": received
                }]
        }]})
if telegramtoken != "":
    resp = requests.post(
        url=f'https://api.telegram.org/bot{telegramtoken}/sendMessage?chat_id={telegramchatid}&text=Client disconnected from vpn with name: {common_name}, ip: {ip}, bytes sent: {bytes_sent} and bytes recieved: {bytes_received}').json()