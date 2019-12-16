import requests
import json
import time

## Handles API Calls
def api(symbol):
    request = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=pk_fc4857bc809645fb98c7bfa9132d259d'
    return request

## Presents JSON from API in a user-friendly format
def jsonToStock(jsonObj):
    stockDict = json.loads(jsonObj)
    print("Symbol:", stockDict["symbol"])
    print("Price:", stockDict["latestPrice"])
    print("Company Name:", stockDict["companyName"])
    print("--------------------")


end = False
count = 0

# Loop contains controls for program
while end is False:
    count = count + 1
    print("Current Count :", count)

    stockResponse = requests.get(api("F"))
    print(jsonToStock(stockResponse.content))
    time.sleep(2)
