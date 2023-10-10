import os
import requests

# variables
common_name = os.environ['common_name']
ip = os.environ['untrusted_ip']
gotifyurl = ""
gotifytoken = ""
discordurl = ""
telegramtoken = ""
telegramchatid = ""

# main
if gotifyurl != "":
    resp = requests.post(f'{gotifyurl}/message?token={gotifytoken}', json={
        "title": "Client connected to vpn ",
        "message": f"{common_name} {ip}",
        "priority": 10
    })
if discordurl != "":
    resp = requests.post(discordurl, json={
    "embeds": [
        {
            "title": "VPNWATCHDOG",
            "color": 1021530,
            "description": "Client connected",
            "fields": [
                {
                    "name": "Client name:",
                    "value": common_name,
                },
                {
                    "name": "IP:",
                    "value": ip,
                }]
        }]})
if telegramtoken != "":
    resp = requests.post(
        url=f'https://api.telegram.org/bot{telegramtoken}/sendMessage?chat_id={telegramchatid}&parse_mode=html&text=<b><u>VPN client connected</u></b> %0AName: <b><i>{common_name}</i></b> %0AIp: <b><i>{ip}</i></b>').json()