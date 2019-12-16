import requests
import json
import time

## Handles API Calls
def api(symbol):
    request = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=pk_c37812d235954d52b6089fe8ecf50261'
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