import sst as SMART
import account as ACT
import transaction as TRAN
import stock as STOCK
import sstconfig

def createAccount():
    account = ACT.Account()
    account.initializeAccount(5000, ['F','AAPL'], [], '')
    return account

config = sstconfig.SSTConfig(2)

account = createAccount()

smartTrader = SMART.SST(account,config)

smartTrader.watch()