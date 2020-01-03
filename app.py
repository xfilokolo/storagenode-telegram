from urllib import request
import json
import requests

# CONFIG-BEGIN
storagenode_name = 'YOUR_STORAGENODE_NAME'
node_ip = 'YOUR_NODE_IP_ADDRESS'
bot_token = 'YOUR_TELEGRAM_BOT_API_TOKEN_FROM_BOTFATHER'
bot_chatID = 'YOUR_CHAT-ID_FROM_USERINFOBOT'
# CONFIG-END

# DISK SPACE
with request.urlopen(f'http://{node_ip}:14002/api/dashboard') as url:
    data = json.loads(url.read().decode())
    used_space = (data['data']['diskSpace']['used']/1000000000)
    available_space = (data['data']['diskSpace']['available']/1000000000)
    free_space = round(available_space - used_space, 4)

# BANDWIDTH
with request.urlopen(f'http://{node_ip}:14002/api/satellites') as url:
    data = json.loads(url.read().decode())
    uploaded = round(data['data']['egressSummary']/1000000000, 2)
    downloaded = round(data['data']['ingressSummary']/1000000000, 2)

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

telegram_bot_sendtext(
    "`"
    f"------{storagenode_name}------\n"
    f"Disk Remaining: {free_space} GB\n"
    f"Uploaded: {uploaded} GB\n"
    f"Downloaded: {downloaded} GB\n"
    "`"
)