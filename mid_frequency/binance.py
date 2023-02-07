from binance.client import Client
import time

# got the message: Your IP address shows that you are attempting to access our services from a restricted jurisdiction. We are unable to provide services to users in your region and apologise for any inconvenience caused.
with open("API_key") as file:
    api_key = file.readline()
    api_secret = file.readline()
client = Client(api_key, api_secret)

# last trades made for BTCUSDT in the last 5 minutes and calculates the Volume-Weighted Average Price (VWAP)

# get the latest trades for BTCUSDT in the last 5 minutes
last_5_minutes = int(time.time() * 1000) - (5 * 60 * 1000)
trades = client.get_recent_trades("BTCUSDT", startTime=last_5_minutes)

# calculate VWAP
vwap = 0
volume = 0
for trade in trades:
    volume += trade['quoteQty'] * trade['price']
    vwap += trade['quoteQty']

vwap = volume / vwap

print("Volume-Weighted Average Price (VWAP) for BTCUSDT in the last 5 minutes:", vwap)