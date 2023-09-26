import os
import requests

# variables
common_name = os.environ['common_name']
ip = os.environ['untrusted_ip']
url = ""

data = {
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
        }
    ]
}

# main script
rl = requests.post(url, json=data)