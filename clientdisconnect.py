import os
import requests

# variables
common_name = os.environ['common_name']
ip = os.environ['untrusted_ip']
recieved = os.environ['bytes_received']
send = os.environ['bytes_sent']
url = ""

data = {
    "embeds": [
        {
            "title": "VPNWATCHDOG",
            "color": 11144204,
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
                    "name": "Bytes recieved:",
                    "value": recieved,
                },
                {
                    "name": "Bytes send:",
                    "value": send,
                }]
        }
    ]
}

# main script
rl = requests.post(url, json=data)