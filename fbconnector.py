import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./keys/adminsdk.txt")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

def getAccountRef(accountID):
    return db.collection(u'accounts').document(accountID)

def getTransactionRef(accountID):
    return db.collection(u'transactions').document(accountID)

def getShareRef(accountID):
    return db.collection(u'shares').document(accountID)

def getConfigRef(accountID):
    return db.collection(u'config').document(accountID)

def setAccount(account):
    getAccountRef(account.accountID).set({
        u'accountID': account.accountID,
        u'capital': account.capital,
        u'stocks': account.stocks
    })

def setTransactions(transactions, accountID):
    getTransactionRef(accountID).set({
        u'accountID': accountID,
        u'transactions': transactions
    })

def setShares(shares, accountID):
    getShareRef(accountID).set({
        u'accountID': accountID,
        u'shares': shares
    })

def setConfig(config, accountID):
    getConfigRef(accountID).set({
        u'accountID': accountID,
        u'latency': config.latency
    })

def getAccount(account):
    doc = getAccountRef(account.accountID)
    accountDict = doc.get()
    print(u'Document data: {}'.format(accountDict.to_dict()))

def getTransaction(accountID):
    doc = getTransactionRef(accountID)
    transactionDict = doc.get()
    print(u'Document data: {}'.format(transactionDict.to_dict()))

def getShare(accountID):
    doc = getShareRef(accountID)
    shareDict = doc.get()
    print(u'Document data: {}'.format(shareDict.to_dict()))

def getConfig(accountID):
    doc = getConfigRef(accountID)
    shareDict = doc.get()
    print(u'Document data: {}'.format(shareDict.to_dict()))