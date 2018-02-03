#Testing coinmarket API
import urllib.request
import json

#get request from coin market api
f = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/")
coins = json.loads(f.read()) #converts to JSON
for coin in coins:
        if(coin['id'] == "bitcoin"): #finds Bitcoin
                print("Bitcoin")
		
