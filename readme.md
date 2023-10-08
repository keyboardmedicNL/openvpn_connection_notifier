# what is it
2 simple scripts that are called by the openvpn config when a client connects or disconnect wich send a message to a discord webhook to notify you someone connected or disconnected. it shows the ip and profile used on connect and ip, profile used, bytes recieved and bytes send on disconnect

# how to use
1. add your webhook url to the url variable in the scripts (leave empty if you do not intent to use a certain notification service)
example (uses only discord to notify):
    ```
    # variables
    common_name = os.environ['common_name']
    ip = os.environ['untrusted_ip']
    gotifyurl = ""
    gotifytoken = ""
    discordurl = "blabla_im_a_url"
    telegramtoken = ""
    telegramchatid = ""
    ```
2. apply the right ownership permissions to the files otherwise openvpn can not run them (default is openvpn on linux)
3. set the scrips to be called in your openvpn server.conf by adding the lines:
```
script-security 2
client-connect "/usr/bin/python /path/to/script/clientconnect.py"
client-disconnect "/usr/bin/python /path/to/script/clientdisconnect.py"
```
* script-security allows openvpn to run and use 3rd party script
* client-connect triggers on a client connecting
* client-disconnect triggers on a client disconnecting
4. restart openvpn and test