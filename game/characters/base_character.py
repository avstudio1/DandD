# base_character.py
# Updated 2018-12-01
# Justin Wood

class base_character:

    char_races = {
        'Dwarf' : [' Bold, hardy, warrior, miner, long memory and grudges.'],
        'Mountain Dwarf' : [' Strong, hardy, rugged, tall for a dwarf.'],
        'Hill Dwarf' : [' Keen senses, deep intuition, remarkable resilience.'],
        'Elf' : [' Magical people of otherworldly grace, in but not of the world.'],
        'Wood Elf' : [' Keen senses and intuition, fleet feet, and stealth.'],
        'High Elf' : [' Keen mind and master of basic magic.'],
        'Drow' : [' Follow the god Lolth down the path of evil and corruption.'],
        'Halfling' : [' You love peace, food, hearth, and home.'],
        'Lightfoot Halfling' : [' You can easily hide, are inclined to get along with others.'],
        'Stout Halfling' : [' Hardier than average and may be part dwarven blood.'],
        'Human' : [' Young, short lived race, innovators and achievers.'],
        'Dragonborn' : [' A servant to dragons, a warrior, or a drifter.'],
        'Gnome' : [' You delight in life, are an inventor, explorer, and explorer.'],
        'Forest Gnome' : [' Knack for illusion and inherent quickness and stealth.'],
        'Half-Elf' : [' Curious, inventive, ambitious, love nature, artistic.'],
        'Half-Orc' : [' Adventurer with savage fury and barbaric customs.'],
        'Tiefling' : [' Demonic heritage, self-reliant, suspicious, drifter.'],
        }

    char_classes = {
        'Barbarian' : ['The relentless combatant fueled by fury.'],
        'Bard' : ['The musical entertainer or somewhat witty storyteller.'],
        'Cleric' : ['The holy man and spiritual healer.'],
        'Druid' : ['The nomad who is devoted to the powers of nature'],
        'Fighter' : ['The skilled combatant and strategist'],
        'Monk' : ['The martial artist and master of the bodily powers.'],
        'Paladin' : ['The novice fighter bolstered by divine magic.'],
        'Ranger' : ['The hunter that combines knowledge of nature with and martial acuity.'],
        'Rogue' : ['The stealthy thief or assassin.'],
        'Sorcerer' : ['The magic user that  power from within.'],
        'Warlock' : ['The conjurer that makes pacts with lesser deities.'],
        'Wizard' : ['The keeper of arcane secrets and worker of magic.'],
        }
        
    char_abilities = {
        'Strength' : ['power', 'melee damage'],
        'Dexterity' : ['agility', 'reflex', 'balance', 'poise'],
        'Constitution' : ['health', 'stamina', 'vitality'],
        'Intelligence' : ['analytical', 'memory', 'cognition'],
        'Wisdom' : ['awareness', 'intuititiive', 'insightful'],
        'Charisma' : ['confident', 'eloquence', 'leadership'],
        }

    def __init__(self, char_race, char_class):
        self.char_race = char_race
        self.char_class = char_class

    def getChar(self):
        return "You are a " + self.char_race + " " + self.char_class
