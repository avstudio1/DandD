# purse.py
# Dec. 28, 2016
# Justin Wood

import coin

class purse:
    def __init__(self, account={'cp': 0, 
                                'sp': 0, 
                                'ep': 0,
                                'gp': 0,
                                'pp': 0
                                }, 
                                numCoins=0, mass=0):
        self.account = account
        self.numCoins = numCoins
        self.mass = mass
        self.cp = coin.cp()
        self.sp = coin.sp()
        self.ep = coin.ep()
        self.gp = coin.gp()
        self.pp = coin.pp()
        self.purse = {'cp': self.cp, 
                      'sp': self.sp, 
                      'ep': self.ep, 
                      'gp': self.gp, 
                      'pp': self.pp
                      }

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
