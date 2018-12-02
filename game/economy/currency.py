# currency.py
# Updated 2018-12-01
# Justin Wood

coin_types = {'cp': 0,
                  'sp': 0,
                  'ep': 0,
                  'gp': 0,
                  'pp': 0
                  }


''' Define a container for holding game currencies.'''
class purse:


    ''' When a new purse is created, the coin type, weights
    and colors are created for that purse instance.  '''
    def __init__(self, color='brown', account= coin_types, numCoins=0, mass=0):
        self.color = color
        self.account = account
        self.numCoins = numCoins
        self.mass = mass
        self.cp = cp()
        self.sp = sp()
        self.ep = ep()
        self.gp = gp()
        self.pp = pp()
        self.purse = {'cp': self.cp, 
                      'sp': self.sp, 
                      'ep': self.ep, 
                      'gp': self.gp, 
                      'pp': self.pp
                      }

    ''' Method to update the value of all held coins in purse
    whenever a transaction occurs. Use refreshPurse() to
    display the contents and weight of your purse. '''
    def refreshPurse(self):
#        ackPurse = ''
#        prevNumCoins = self.numCoins
#        previousMass = self.mass
        self.numCoins = 0
        self.mass = 0
        
        for k, v in self.purse.items():
            self.account[k] = v.value
            self.numCoins += v.value
            self.mass += (v.value * v.weight)

        print(self.account)
        print("Purse weighs: " + str(self.mass))

    ''' Method to exchange coins from one type to another.'''
    def exchangeP(self, exchAmount, exchFrom, exchTo):
        self.exchAmount = exchAmount
        self.exchFrom = exchFrom
        self.exchTo = exchTo
        exchTypes = {'cp':0,'sp':1,'ep':2,'gp':3,'pp':4}
        exchTable = {'cp':[1,0.1,0.02,0.01,0.001],
                     'sp':[10,1,0.2,0.1,0.01],
                     'ep':[50,5,1,0.5,0.05],
                     'gp':[100,10,2,1,0.1],
                     'pp':[1000,100,20,10,1]
                     }

        for _k, _v in exchTable.items():
            exchCurrent = exchTable.get(self.exchFrom)
            
        for _k, _v in exchTypes.items():
            exchToType = exchTypes.get(self.exchTo)

        exchTransaction = exchCurrent[exchToType] * self.exchAmount
       
        if getattr(self, self.exchFrom).value < self.exchAmount:
            return "Not enough " + self.exchFrom
        elif exchTransaction < 1:
            return "Cannot break coins apart!"
        else:
            _exchFromNew = getattr(self, self.exchFrom).value - self.exchAmount
            _exchToNew = getattr(self, self.exchTo).value + exchTransaction
            
            _exchFromResult = getattr(self, self.exchFrom).putP(self.exchAmount)
            _exchToResult = getattr(self, self.exchTo).getP(exchTransaction)
        
        return "Exchanged " + str(self.exchAmount) + \
                " " + str(self.exchFrom) + \
                " for " + str(exchTransaction) + \
                " " + str(self.exchTo)

''' Defines the types of coins available in game.
    Each coin has value, weight and color attributes. '''
class coin:

    ''' Each time a coin is created it contains the
        value and weight of the coin. '''    
    def __init__(self, coinType, color, weight, value):
        self.coinType = coinType
        self.value = value
        self.weight = weight

    ''' Method to add coins. '''
    def getP(self, otherP):
        self.value += otherP 
        self.mass = otherP * self.weight

    ''' Method to give coins. '''
    def putP(self, otherP):
        brokeP = "You don't have enough " + str(self.coinType)
        a = self.value - otherP
        if a < 0:
            return brokeP
        else:
            self.value = a
            self.mass = a * self.weight

    ''' Method to exchange coins from one type to another. '''
    def exchangeP(self, exchAmount, exchFrom, exchTo):
        self.exchAmount = exchAmount
        self.exchFrom = exchFrom
        self.exchTo = exchTo
        exchTypes = {'cp':0,'sp':1,'ep':2,'gp':3,'pp':4}
        exchTable = {'cp':[1,0.1,0.02,0.01,0.001],
                     'sp':[10,1,0.2,0.1,0.01],
                     'ep':[50,5,1,0.5,0.05],
                     'gp':[100,10,2,1,0.1],
                     'pp':[1000,100,20,10,1]
                     }

        for _k, _v in exchTable.items():
            exchCurrent = exchTable.get(self.exchFrom)

        for _k, _v in exchTypes.items():
            exchToType = exchTypes.get(self.exchTo)

        exchTransaction = exchCurrent[exchToType] * self.exchAmount
        return exchTransaction

''' Specifies cp coin type = copper '''
class cp(coin):
    def __init__(self, coinType="Copper", color="Reddish", weight=2, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

''' Specifies sp coin type = silver '''
class sp(coin):
    def __init__(self, coinType="Silver", color="Scaly White", weight=5, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

''' Specifies ep coin type = electrum '''
class ep(coin):
    def __init__(self, coinType="Electrum", color="Blueish", weight=3, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

''' Specifies gp coin type = gold '''
class gp(coin):
    def __init__(self, coinType="Gold", color="Gold", weight=7, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

''' Specifies pp coin type = platinum '''
class pp(coin):
    def __init__(self, coinType="Platinum", color="Brilliant White", weight=10, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

''' Create a new purse with some coins '''
def create_purse(purse_owner):
    new_purse = purse()
    new_purse.cp.getP(100)
    new_purse.sp.getP(50)
    new_purse.ep.getP(20)
    new_purse.gp.getP(5)
    new_purse.refreshPurse()
    account_purse = {purse_owner: new_purse}
    return account_purse

