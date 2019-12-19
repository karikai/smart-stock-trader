import sst as SMART
import account as ACT
import transaction as TRAN
import stock as STOCK
import sstconfig
import fbconnector as FIRE

def createAccount():
    account = ACT.Account()
    account.initializeAccount(5000, ['F','AAPL'], [], 'newerAccount')
    initializeFirebase(account)
    return account

def initializeFirebase(account):
    config = sstconfig.SSTConfig(2)
    FIRE.setAccount(account)
    FIRE.setTransactions(account.transactions, account.accountID)
    FIRE.setShares(account.shares, account.accountID)
    FIRE.setConfig(config, account.accountID)

config = sstconfig.SSTConfig(2)

account = createAccount()

smartTrader = SMART.SST(account,config)

smartTrader.watch()