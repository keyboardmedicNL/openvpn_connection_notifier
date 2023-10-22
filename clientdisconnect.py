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
telegramtoken = ""
telegramchatid = ""

#converts bytes to mb,gb,etc
def convert_bytes(num):
    step_unit = 1000.0
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit

# main
bytesformsent = convert_bytes(int(sent))
bytesformrec = convert_bytes(int(received))
if gotifyurl != "":
    resp = requests.post(f'{gotifyurl}/message?token={gotifytoken}', json={
        "title": "Client disconnected from vpn ",
        "message": f"{common_name} {ip} data sent: {bytesformsent} data received: {bytesformrec}",
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
                    "name": "Data sent:",
                    "value": bytesformsent,
                },
                {
                    "name": "Data received:",
                    "value": bytesformrec
                }]
        }]})
if telegramtoken != "":
    resp = requests.post(
        url=f'https://api.telegram.org/bot{telegramtoken}/sendMessage?chat_id={telegramchatid}&parse_mode=html&text=<b><u>VPN client disconnected</u></b> %0AName: <b><i>{common_name}</i></b> %0AIp: <b><i>{ip}</i></b> %0AData sent: <b><i>{bytesformsent}</i></b> %0AData recieved: <b><i>{bytesformrec}</i></b>').json()