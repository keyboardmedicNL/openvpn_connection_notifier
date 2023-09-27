import os
import requests

# variables
common_name = os.environ['common_name']
ip = os.environ['untrusted_ip']
gotifyurl = ""
gotifytoken = ""
discordurl = ""

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