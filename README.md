# Storj's Storagenode Telegram Monitoring
This simple app allows you to get most important stats of your node directly to your Telegram! <br>
[Storj on Github](https://github.com/storj/storj)

Now displays the value changes since the last check!

![Screen of sample Telegram message](https://i.imgur.com/Hyq4IEq.png)

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
nodeIp = '---CHANGE-ME---'
botToken = '---CHANGE-ME---'
botChatId = '---CHANGE-ME---'
currency = 'USD'
```
1. `nodeIp` - Only IP, don't put here port or full dashboard URL. Local or Public node IP. If you running this app in the same network in wchich your node is running use node's local IP. If you running app from other network use public IP of your node.
2. `botToken` - Token from [@BotFather](https://t.me/BotFather)
3. `botChatId` - Chat ID from [@userinfobot](https://t.me/userinfobot)
4. `currency` - Your prefered currency to calculate earnings (USD/EUR/PLN/CNY or others). 

- Now config is completed. Save file and run using Python 3.

### Other info
- You can use Crontab to schedule automated raports. 
- Upload / download stats from full current period (like in web dashboard).
- lastX.txt file is storage for last values. Keep them in same folder with `app.py`.
