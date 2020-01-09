import sst as SMART
import account as ACT
import transaction as TRAN
import stock as STOCK
import sstconfig as CONFIG
import fbconnector as FIRE

def createAccount():
    account = ACT.Account()
    account.initializeAccount(5000, ['F','AAPL'], [], 'newerAccount', [])
    initializeFirebase(account)
    return account

def initializeFirebase(account):
    config = CONFIG.SSTConfig(2)
    FIRE.setAccount(account)
    FIRE.setTransactions(account.transactions, account.accountID)
    FIRE.setShares(account.shares, account.accountID)
    FIRE.setConfig(config, account.accountID)

def getAccount(accountID):
    account = ACT.Account()
    accountResponse = FIRE.getAccount(accountID)
    transactionResponse = FIRE.getTransaction(accountID)
    shareResponse = FIRE.getShare(accountID)

    account.initializeAccount(accountResponse['accountID'], accountResponse['stocks'], transactionResponse['transactions'],
    accountResponse['accountID'], shareResponse['shares'])
    return account


account = getAccount('newerAccount')

print(account)

config = CONFIG.SSTConfig(2)

smartTrader = SMART.SST(account,config)

smartTrader.watch()