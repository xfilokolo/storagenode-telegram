# Storj's Storagenode Telegram Monitoring
This simple app allows you to get most important stats of your node directly to your Telegram! <br>
[Storj on Github](https://github.com/storj/storj)

![Screen of sample Telegram message](https://i.imgur.com/SJovBcG.png)

### What you need to prepare?
- Storagenode IP address
- Create your own Telegram bot (that's easy :D )
- Check your Telegram chatID
- YOUR NODE DASHBOARD NEED TO BE RUNNING! [How to run dashboard](https://documentation.storj.io/setup/cli/dashboard)

### Installation 
- Download this repo using: <br>
```git clone https://github.com/xfilokolo/storagenode-telegram.git```

- Talk with [@BotFather](https://t.me/BotFather) in your Telegram app.

- Press start and type `/newbot` to start creating your bot. Follow instructions in Telegram.

- Now talk with [@userinfobot](https://t.me/userinfobot) and press `/start`.

- Edit `app.py` from this repo using your prefered text editor and fill config:
```python
# CONFIG-BEGIN
storagenode_name = 'YOUR_STORAGENODE_NAME'
node_ip = 'YOUR_NODE_IP_ADDRESS'
bot_token = 'YOUR_TELEGRAM_BOT_API_TOKEN_FROM_BOTFATHER'
bot_chatID = 'YOUR_CHAT-ID_FROM_USERINFOBOT'
# CONFIG-END
```
1. `YOUR_STORAGENODE_NAME` - Your invented node name (any)
2. `YOUR_NODE_IP_ADDRESS` - Only IP, don't put here port or full dashboard URL. Local or Public node IP. If you running this app in the same network in wchich your node is running use node's local IP. If you running app from other network use public IP of your node.
3. `YOUR_TELEGRAM_BOT_API_TOKEN_FROM_BOTFATHER` - Token from [@BotFather](https://t.me/BotFather)
4. `YOUR_CHAT-ID_FROM_USERINFOBOT` - Chat ID from [@userinfobot](https://t.me/userinfobot)

- Now config is completed. Save file and run using Python 3.
- You can use Crontab to schedule automated raports. 
- Upload / download stats from full current period (like in web dashboard)
