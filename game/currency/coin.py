# coin.py
# Dec. 27, 2016

class coin:

    def __init__(self, coinType, color, weight, value):
        self.coinType = coinType
        self.value = value
        self.weight = weight

    def getP(self, otherP):
        self.value += otherP 
        self.mass = otherP * self.weight

    def putP(self, otherP):
        brokeP = "You don't have enough " + str(self.coinType)
        a = self.value - otherP
        if a < 0:
            return brokeP
        else:
            self.value = a
            self.mass = a * self.weight

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

class cp(coin):
    def __init__(self, coinType="Copper", color="Reddish", weight=2, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

class sp(coin):
    def __init__(self, coinType="Silver", color="Scaly White", weight=5, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

class ep(coin):
    def __init__(self, coinType="Electrum", color="Blueish", weight=3, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

class gp(coin):
    def __init__(self, coinType="Gold", color="Gold", weight=15, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

class pp(coin):
    def __init__(self, coinType="Platinum", color="Brilliant White", weight=10, value=0):
        self.coinType = coinType
        self.color = color
        self.weight = weight
        self.value = value
        self.mass = 0

    


