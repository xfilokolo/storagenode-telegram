from urllib import request
import json
import requests

# CONFIG-BEGIN
nodeIp = '---CHANGE-ME---'
botToken = '---CHANGE-ME---'
botChatId = '---CHANGE-ME---'
currency = 'USD'
# CONFIG-END

# STORJ to CURRENCY
with request.urlopen(f'https://api.coinpaprika.com/v1/tickers/storj-storj?quotes={currency}') as url:
    data = json.loads(url.read().decode())
    storjToCurrency = (data['quotes'][f'{currency}']['price'])

# STORJ to USD
with request.urlopen('https://api.coinpaprika.com/v1/tickers/storj-storj?quotes=USD') as url:
    data = json.loads(url.read().decode())
    storjToUsd = (data['quotes']['USD']['price'])

# USD to CURRENCY
with request.urlopen('https://api.exchangeratesapi.io/latest?base=USD') as url:
    data = json.loads(url.read().decode())
    storjToCurrency = (data['rates'][f'{currency}'])

# DISK SPACE
with request.urlopen(f'http://{nodeIp}:14002/api/dashboard') as url:
    data = json.loads(url.read().decode())
    usedSpace = (data['data']['diskSpace']['used']/1000000000)
    availableSpace = (data['data']['diskSpace']['available']/1000000000)
    freeSpace = round(availableSpace - usedSpace, 4)

# BANDWIDTH
with request.urlopen(f'http://{nodeIp}:14002/api/satellites') as url:
    data = json.loads(url.read().decode())
    uploaded = round(data['data']['egressSummary']/1000000000, 2)
    downloaded = round(data['data']['ingressSummary']/1000000000, 2)

payoutUsd = (uploaded / 1000 * 20)
payoutCurrency = (payoutUsd * storjToCurrency)
payoutStorj = (payoutUsd / storjToUsd)

# CHANGE SINCE LAST CHECK
# CHECK LAST VALUES
# DISK
f = open("lastDisk.txt", "r")
lastDisk = (f.read())
f.close()

# UPLOADED
f = open("lastUploaded.txt", "r")
lastUploaded = (f.read())
f.close()

# DOWNLOADED
f = open("lastDownloaded.txt", "r")
lastDownloaded = (f.read())
f.close()

# STORJ
f = open("lastStorj.txt", "r")
lastStorj = (f.read())
f.close()

# CURRENCY
f = open("lastCurrency.txt", "r")
lastCurrency = (f.read())
f.close()

# PUT NEW VALUES
# DISK
f = open("lastDisk.txt", "w+")
f.write(f"{freeSpace}")
f.close()

# UPLOADED
f = open("lastUploaded.txt", "w+")
f.write(f"{uploaded}")
f.close()

# DOWNLOADED
f = open("lastDownloaded.txt", "w+")
f.write(f"{downloaded}")
f.close()

# STORJ
f = open("lastStorj.txt", "w+")
f.write(f"{payoutStorj}")
f.close()

# CURRENCY
f = open("lastCurrency.txt", "w+")
f.write(f"{payoutCurrency}")
f.close()

# COMPARE OLD AND CURRENT VALUES
changeDisk = freeSpace - float(lastDisk)
changeUploaded = uploaded - float(lastUploaded)
changeDownloaded = downloaded - float(lastDownloaded)
changeStorj = payoutStorj - float(lastStorj)
changeCurrency = payoutCurrency - float(lastCurrency)

# SEND IT
def telegram_bot_sendtext(bot_message):
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatId + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(sendText)
    return response.json()

telegram_bot_sendtext(
    "`"
    f"------{nodeIp}------\n"
    f"Disk Remaining: {freeSpace} ({round(changeDisk, 2)}) GB\n"
    f"Uploaded: {uploaded} ({round(changeUploaded, 2)}) GB\n"
    f"Downloaded: {downloaded} ({round(changeDownloaded, 2)}) GB\n\n"
    "Payout:\n"
    f"{round(payoutStorj, 2)} ({round(changeStorj, 2)}) STORJ\n"
    f"{round(payoutCurrency, 2)} ({round(changeCurrency, 2)}) {currency}\n"
    "`"
)