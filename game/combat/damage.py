# damage.py
# Dec. 29, 2016
import dice

class damage:
    ''' Each creature that does damage will have a base damage type
        and modifier that will not change for that round of combat '''
    def __init__(self, dmgType, baseDiceConfig, modDiceConfig):
        self.baseDiceConfig = baseDiceConfig
        self.modDiceConfig = modDiceConfig
        self.dmgType = dmgType
        
    def doDamage(self, otherDiceConfig):
        self.otherDiceConfig = otherDiceConfig
        dmgTypeTable = {'Acid':['Corrosion'],
                'Bludgeoning':['Trauma'],
                'Water':['Chilled'],
                'Fire':['Scorched'],
                'Quint':['Magic'],
                'Lightning':['Electric'],
                'Necrotic':['Confidence'],
                'Piercing':['Punctured'],
                'Slashing':['Torn'],
                'Thunder':['Concussive']
                }
        
        baseDamage = dice.roll(self.baseDiceConfig)
        modDamage = dice.roll(self.modDiceConfig)
        for _k, _v in dmgTypeTable.items():
            modEffect = dmgTypeTable.get(self.dmgType)[0]
        return "Base dmg: " + str(int(baseDamage)) +\
               ", and " + str(modEffect) +\
               " dmg: " + str(int(modDamage))

