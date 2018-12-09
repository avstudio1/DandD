#!/usr/bin/python
from __future__ import print_function, division


###########
# Imports #
###########

import sys
import math
import random
import itertools

try:
    # Use the system PRNG if possible
    random = random.SystemRandom()
except NotImplementedError:
    import warnings
    warnings.warn("A secure pseudo-random number generator is not available "
                  "on your system. Falling back to Mersenne Twister.")

# Python 2 compatibility
try:
    range = xrange
    input = raw_input
except NameError:
    pass


##########################
# Lists and Dictionaries #
##########################


cr_xp = expand({
    0: 10,
    1 / 8: 25,
    1 / 4: 50,
    1 / 2: 100,
    1: 200,
    2: 450,
    3: 700,
    4: 1100,
    5: 1800,
    6: 2300,
    7: 2900,
    8: 3900,
    9: 5000,
    10: 5900,
    11: 7200,
    12: 8400,
    13: 10000,
    14: 11500,
    15: 13000,
    16: 15000,
    17: 18000,
    18: 20000,
    19: 22000,
    20: 25000,
    21: 33000,
    22: 41000,
    23: 50000,
    24: 62000,
    25: 75000,
    26: 90000,
    27: 105000,
    28: 120000,
    29: 135000,
    30: 155000,
})

item_loot = []

card_deck = [
    "Hooded One (7)    ",
    "Enchanter (3)     ",
    "Shepherd (4)      ",
    "Tempter           ",
    "Raven             ",
    "Seer              ",
    "Swashbuckler (1)  ",
    "Executioner       ",
    "Ghost             ",
    "Warrior           ",
    "Tax Collector (8) ",
    "Anarchist (6)     ",
    "Marionette        ",
    "Miser (9)         ",
    "Torturer (9)      ",
    "Priest            ",
    "Traitor (9)       ",
    "Paladin (2)       ",
    "Thief (7)         ",
    "Beast             ",
    "Guild Member (5)  ",
    "Healer (3)        ",
    "Darklord          ",
    "Myrmidon (5)      ",
    "Elementalist (5)  ",
    "Diviner (2)       ",
    "Abjurer (4)       ",
    "Artifact          ",
    "Avenger (1)       ",
    "Beggar (6)        ",
    "Beserker (6)      ",
    "Bishop (8)        ",
    "Broken One        ",
    "Charlatan (7)     ",
    "Conjurer (9)      ",
    "Dictator (8)      ",
    "Donjon            ",
    "Druid (5)         ",
    "Evoker (6)        ",
    "Horseman          ",
    "Illusionist (7)   ",
    "Innocent          ",
    "Missionary (2)    ",
    "Mists             ",
    "Monk (1)          ",
    "Necromancer (8)   ",
    "Philanthropist (2)",
    "Rogue             ",
    "Soldier (3)       ",
    "Trader (3)        ",
    "Transmuter (1)    ",
    "Wizard            ",
    "Mercenary (4)     ",
    "Merchant (4)      "
]



race_short = [
    "Dwarf", "Mountain Dwarf", "Hill Dwarf", "Elf", "Wood Elf", "High Elf", "Drow", "Halfling", "Lightfoot Halfling", "Stout Halfling", "Human", "Dragonborn", "Gnome", "Forest Gnome", "Half-Elf", "Half-Orc", "Tiefling"
]


    

# Class Descriptions - https://redd.it/2e9vzl

class_short = [
    "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
]

# NPC Class Info - http://www.5esrd.com/gamemastering/monsters-foes/npc/

class_npc = [
    "Acolyte", "Archmage", "Assassin", "Bandit Captain", "Bandit Lord", "Bandit / Pirate", "Berserker", "Black Knight Commander", "City Watch Captain", "Commoner", "Cult Fanatic", "Cult Leader", "Cult Sorcerer", "Cultist", "Devilbound Gnomish Prince", "Druid", "Dwarven Ringmage", "Elvish Veteran Archer", "Ghost Knight", "Gladiator", "Guard", "Half-Red Dragon Veteran", "Knight", "Mage", "Noble", "Corrupted Ogre Chieftain", "Priest", "Ratfolk Rogue", "Scorpion Cultist", "Scout", "Spy", "Thug", "Tribal Warrior", "Veteran", "Wolf Reaver Dwarf"
]

culture_npc = [
    "Babylonian", "Celtic", "Egyptian", "Greek", "Roman", "Sumerian", "English", "French", "German", "Italian", "Norse", "Saxon", "Slavic", "Spanish", "Arabic", "Chineese", "Hebrew", "Hindu", "Japanese", "Mongolian", "Persian", "Congolese", "Etheopian", "Malian", "Algonquin", "Aztec", "Inkan", "Inuit", "Navajo", "Sioux"
]

avg_stats = [
    "   Race        Hieght  Weight         Lifespan",
    "   ----        ------  ------         --------",
    "   Dwarf       4-5'    150 lbs.         350 years",
    "   Elf         5-6'+   150-170 lbs.     750 years",
    "   Halfling    3-4'    40 lbs.          150 years",
    "   Human       5-6'    130-200 lbs.   < 100 years",
    "   Dragonborn  > 6'    250 lbs.       < 100 years",
    "   Gnome       3-4'    40 lbs.          350 years",
    "   Half-Elf    5-6'    130-170 lbs.     180 years",
    "   Half-Orc    5-6'+   150-230 lbs.   < 80 years",
    "   Tiefling    5-6'    130-200 lbs.     100 years"
]




#############
# Functions #
#############

def start_fn():
    print("")
    print("        What would you like to do?          ")
    print("        1) (C)reate Character / NPC         ")
    print("        2) (R)oll Dice                      ")
    print("        3) Roll Initiative (raw)            ")
    print("        4) Encounter Experience Calculator  ")
    print("        5) Get Treasure!                    ")
    print("        6) Tarokka Fortune Cards            ")
    print("        7) Wild Magic (Roll Effect)         ")
    print("        0) (Q)uit                           ")
    print("")
    option = input("What would you like to do? ")
    if option in ("C", "c", "1"):
        global char_name
        global plyr_name
        char_name = ""
        plyr_name = ""
        print("")
        race_fn()
        print("")
        class_fn()
        print("")
        height_fn()
        print("")
        weight_fn()
        print("")
        age_fn()
        print("")
        gender_fn()
        print("")
        abilities_fn()
        print("")
        race_bonus_fn()
        print("")
        modifiers_fn()
        print("")
        saves_fn()
        print("")
        skills_fn()
        print("")
        hp_fn()
        print("")
        alignment_fn()
        print("")
        summary_fn()
        print("")
        name_fn()
        print("")
        save_fn()
    elif option in ("R", "r", "2"):
        dice = int(input("How many dice? "))
        sides = int(input("How many sides on each die? "))
        for _ in itertools.repeat(None, dice):
            print(random.randrange(1, sides))
            start_fn()
    elif option == "3":
        n_players = int(input("How many initiative rolls (e.g. players + monsters)? "))
        for _ in itertools.repeat(None, n_players):
            print(random.randint(1, 20))
        start_fn()
    elif option == "4":
        encounter_fn()
        start_fn()
    elif option == "5":
        loot_menu_fn()
    elif option == "6":
        draw_cards_fn()
        reveal_cards_fn()
        start_fn()
    elif option == "7":
        wild_magic_fn()
        start_fn()
    elif option in ("Q", "q", "0"):
        quit()
    else:
        start_fn()

def loot_cr1_fn():
    gem_n = 0
    gem_t = "0"
    item_loot = []
    d100 = random.randint(1, 100)
    if d100 <= 6:
        pass
    elif 6 < d100 <= 16:
        roll = random.randint(1, 12)
        gem_t = gem_10[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
    elif 16 < d100 <= 26:
        roll = random.randint(1, 10)
        gem_t = art_25[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
    elif 26 < d100 <= 36:
        roll = random.randint(1, 12)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
    elif 36 < d100 <= 44:
        roll = random.randint(1, 12)
        gem_t = gem_10[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for n in range(item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 44 < d100 <= 52:
        roll = random.randint(1, 10)
        gem_t = art_25[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for n in range(item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 52 < d100 <= 60:
        roll = random.randint(1, 12)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for n in range(item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 60 < d100 <= 65:
        roll = random.randint(1, 12)
        gem_t = gem_10[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for n in range(item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 65 < d100 <= 70:
        roll = random.randint(1, 10)
        gem_t = art_25[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for n in range(item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 70 < d100 <= 75:
        roll = random.randint(1, 12)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
            item_n = random.randint(1, 4)
        for n in range(item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 75 < d100 <= 78:
        roll = random.randint(1, 12)
        gem_t = gem_10[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for n in range(item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 78 < d100 <= 80:
        roll = random.randint(1, 10)
        gem_t = art_25[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for n in range(item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 80 < d100 <= 85:
        roll = random.randint(1, 10)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for n in range(item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 85 < d100 <= 92:
        roll = random.randint(1, 10)
        gem_t = art_25[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for n in range(item_n):
            item = random.choice(list(item_f))
            item = item_f[item]
            item_loot.append(item)
    elif 92 < d100 <= 97:
        roll = random.randint(1, 12)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for n in range(item_n):
            item = random.choice(list(item_f))
            item = item_f[item]
            item_loot.append(item)
    elif 97 < d100 <= 99:
        roll = random.randint(1, 10)
        gem_t = art_25[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        choice = random.randint(1, 100)
        if choice in (12, 13, 14):
            roll = random.randint(1, 8)
            item = item_g_12[roll]
            item_loot.append(item)
        else:
            item = random.choice(list(item_g))
            item = item_g[item]
            item_loot.append(item)
    elif d100 > 99:
        roll = random.randint(1, 12)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        choice = random.randint(1, 100)
        if choice in (12, 13, 14):
            roll = random.randint(1, 8)
            item = item_g_12[roll]
            item_loot.append(item)
        else:
            item = random.choice(list(item_g))
            item = item_g[item]
            item_loot.append(item)
    else:
        pass
    print(" ")
    print("## Gems, Art, and Items ##")
    print(gem_n, "x ", gem_t)
    for item in item_loot:
        print(item)


def loot_cr5_fn():
    gem_n = 0
    gem_t = "0"
    item_loot = []
    d100 = random.randint(1, 100)
    if d100 <= 4:
        roll = random.randint(1, 10)
        gem_t = art_25[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
    elif 4 < d100 <= 10:
        roll = random.randint(1, 12)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
    elif 10 < d100 <= 16:
        roll = random.randint(1, 12)
        gem_t = gem_50[roll]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
    elif 16 < d100 <= 22:
        roll = random.randint(1, 10)
        gem_t = gem_100[roll]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
    elif 22 < d100 <= 28:
        gem_t = art_250[random.randint(1, 12)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
    elif 28 < d100 <= 32:
        gem_t = art_25[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 32 < d100 <= 36:
        gem_t = art_25[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 36 < d100 <= 40:
        gem_t = gem_100[random.randint(1, 10)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 40 < d100 <= 44:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
    elif 44 < d100 <= 49:
        gem_t = art_25[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 49 < d100 <= 54:
        gem_t = gem_50[random.randint(1, 12)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 54 < d100 <= 59:
        gem_t = gem_100[random.randint(1, 10)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 59 < d100 <= 63:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 63 < d100 <= 66:
        gem_t = art_25[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 63 < d100 <= 69:
        gem_t = gem_50[random.randint(1, 12)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 69 < d100 <= 72:
        gem_t = gem_100[random.randint(1, 10)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 72 < d100 <= 74:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 74 < d100 <= 76:
        gem_t = art_25[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_d))
        item = item_d[item]
        item_loot.append(item)
    elif 76 < d100 <= 78:
        gem_t = gem_50[random.randint(1, 12)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item = random.choice(list(item_d))
        item = item_d[item]
        item_loot.append(item)
    elif d100 == 79:
        gem_t = gem_100[random.randint(1, 10)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item = random.choice(list(item_d))
        item = item_d[item]
        item_loot.append(item)
    elif d100 == 80:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_d))
        item = item_d[item]
        item_loot.append(item)
    elif 80 < d100 <= 84:
        gem_t = art_25[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_f))
            item = item_f[item]
            item_loot.append(item)
    elif 84 < d100 <= 88:
        gem_t = gem_50[random.randint(1, 12)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_f))
            item = item_f[item]
            item_loot.append(item)
    elif 88 < d100 <= 91:
        gem_t = gem_100[random.randint(1, 10)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_f))
            item = item_f[item]
            item_loot.append(item)
    elif 91 < d100 <= 94:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_f))
            item = item_f[item]
            item_loot.append(item)
    elif 94 < d100 <= 96:
        gem_t = gem_100[random.randint(1, 10)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif d100 == 99:
        gem_t = gem_100[random.randint(1, 10)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item = random.choice(list(item_h))
        item = item_h[item]
        item_loot.append(item)
    elif d100 == 100:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_h))
        item = item_h[item]
        item_loot.append(item)
    else:
        pass
    print(" ")
    print("## Gems, Art, and Items ##")
    print(gem_n, "x ", gem_t)
    for item in item_loot:
        print(item)


def loot_cr11_fn():
    item_loot = []
    gem_t = "0"
    gem_n = 0
    d100 = random.randint(1, 100)
    if d100 <= 3:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
    elif 3 < d100 <= 6:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
    elif 6 < d100 <= 9:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
    elif 9 < d100 <= 12:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
    elif 12 < d100 <= 15:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
    elif 15 < d100 <= 19:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 19 < d100 <= 23:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 23 < d100 <= 26:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item))
            item = item_b[item]
            item_loot.append(item)
    elif 26 < d100 <= 29:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_a))
            item = item_a[item]
            item_loot.append(item)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_b))
            item = item_b[item]
            item_loot.append(item)
    elif 29 < d100 <= 35:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 35 < d100 <= 40:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 40 < d100 <= 45:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 45 < d100 <= 54:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 54 < d100 <= 58:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 58 < d100 <= 62:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 62 < d100 <= 66:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 66 < d100 <= 68:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_e))
        item = item_e[item]
        item_loot.append(item)
    elif 68 < d100 <= 70:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_e))
        item = item_e[item]
        item_loot.append(item)
    elif 70 < d100 <= 72:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item = random.choice(list(item_e))
        item = item_e[item]
        item_loot.append(item)
    elif 72 < d100 <= 74:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item = random.choice(list(item_e))
        item = item_e[item]
        item_loot.append(item)
    elif 74 < d100 <= 76:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_f))
        item = item_f[item]
        item_loot.append(item)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif 76 < d100 <= 78:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_f))
        item = item_f[item]
        item_loot.append(item)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif 78 < d100 <= 80:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item = random.choice(list(item_f))
        item = item_f[item]
        item_loot.append(item)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif 80 < d100 <= 82:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item = random.choice(list(item_f))
        item = item_f[item]
        item_loot.append(item)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif 82 < d100 <= 85:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 5)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 85 < d100 <= 88:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 88 < d100 <= 90:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 90 < d100 <= 92:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 92 < d100 <= 94:
        gem_t = art_250[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
            choice = random.randint(1, 100)
            if choice == 76:
                item = random.choice(list(item_i_76))
                item = item_i_76[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_i))
                item = item_i[item]
                item_loot.append(item)
    elif 94 < d100 <= 96:
        gem_t = art_750[random.randint(1, 10)]
        gem_n = 0
        for dice in range(2):
            rolls = random.randint(1, 4)
            gem_n = gem_n + rolls
        item = random.choice(list(item_i))
        item = item_i[item]
        item_loot.append(item)
    elif 96 < d100 <= 98:
        gem_t = gem_500[random.randint(1, 6)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        choice = random.randint(1, 100)
        if choice == 76:
            item = random.choice(list(item_i_76))
            item = item_i_76[item]
            item_loot.append(item)
        else:
            item = random.choice(list(item_i))
            item = item_i[item]
            item_loot.append(item)
    elif 98 < d100:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        choice = random.randint(1, 100)
        if choice == 76:
            item = random.choice(list(item_i_76))
            item = item_i_76[item]
            item_loot.append(item)
        else:
            item = random.choice(list(item_i))
            item = item_i[item]
            item_loot.append(item)
    else:
        pass
    print(" ")
    print("## Gems, Art, and Items ##")
    print(gem_n, "x ", gem_t)
    for item in item_loot:
        print(item)


def loot_cr17_fn():
    item_loot = []
    gem_n = 0
    gem_t = "0"
    d100 = random.randint(1, 100)
    if d100 <= 2:
        pass
    elif 2 < d100 <= 5:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 8)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 5 < d100 <= 8:
        gem_t = art_2500[random.randint(1, 1)]
        gem_n = random.randint(1, 10)
        item_n = random.randint(1, 8)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 8 < d100 <= 11:
        gem_t = art_7500[random.randint(1, 8)]
        gem_n = random.randint(1, 4)
        item_n = random.randint(1, 8)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 11 < d100 <= 14:
        gem_t = gem_5000[random.randint(1, 4)]
        gem_n = random.randint(1, 4)
        item_n = random.randint(1, 8)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_c))
            item = item_c[item]
            item_loot.append(item)
    elif 14 < d100 <= 22:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 22 < d100 <= 30:
        gem_t = art_2500[random.randint(1, 10)]
        gem_n = random.randint(1, 10)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 30 < d100 <= 38:
        gem_t = art_7500[random.randint(1, 8)]
        gem_n = random.randint(1, 4)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 38 < d100 <= 46:
        gem_t = gem_5000[random.randint(1, 4)]
        gem_n = random.randint(1, 8)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_d))
            item = item_d[item]
            item_loot.append(item)
    elif 46 < d100 <= 52:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_e))
            item = item_d[item]
            item_loot.append(item)
    elif 52 < d100 <= 58:
        gem_t = art_2500[random.randint(1, 10)]
        gem_n = random.randint(1, 10)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_e))
            item = item_d[item]
            item_loot.append(item)
    elif 58 < d100 <= 63:
        gem_t = art_7500[random.randint(1, 8)]
        gem_n = random.randint(1, 4)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_e))
            item = item_e[item]
            item_loot.append(item)
    elif 63 < d100 <= 68:
        gem_t = gem_5000[random.randint(1, 4)]
        gem_n = random.randint(1, 8)
        item_n = random.randint(1, 6)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_e))
            item = item_e[item]
            item_loot.append(item)
    elif d100 == 69:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif d100 == 70:
        gem_t = art_2500[random.randint(1, 10)]
        gem_n = random.randint(1, 10)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif d100 == 71:
        gem_t = art_7500[random.randint(1, 8)]
        gem_n = random.randint(1, 4)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif d100 == 72:
        gem_t = gem_5000[random.randint(1, 4)]
        gem_n = random.randint(1, 8)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice in (12, 13, 14):
                item = random.choice(list(item_g_12))
                item = item_g_12[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_g))
                item = item_g[item]
                item_loot.append(item)
    elif 72 < d100 <= 74:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 74 < d100 <= 76:
        gem_t = art_2500[random.randint(1, 10)]
        gem_n = random.randint(1, 10)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 76 < d100 <= 78:
        gem_t = art_7500[random.randint(1, 8)]
        gem_n = random.randint(1, 4)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 78 < d100 <= 80:
        gem_t = gem_5000[random.randint(1, 4)]
        gem_n = random.randint(1, 8)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            item = random.choice(list(item_h))
            item = item_h[item]
            item_loot.append(item)
    elif 80 < d100 <= 85:
        gem_t = gem_1000[random.randint(1, 8)]
        gem_n = 0
        for dice in range(3):
            rolls = random.randint(1, 6)
            gem_n = gem_n + rolls
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice == 76:
                item = random.choice(list(item_i_76))
                item = item_i_76[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_i))
                item = item_i[item]
                item_loot.append(item)
    elif 85 < d100 <= 90:
        gem_t = art_2500[random.randint(1, 10)]
        gem_n = random.randint(1, 10)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice == 76:
                item = random.choice(list(item_i_76))
                item = item_i_76[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_i))
                item = item_i[item]
                item_loot.append(item)
    elif 90 < d100 <= 95:
        gem_t = art_7500[random.randint(1, 8)]
        gem_n = random.randint(1, 4)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice == 76:
                item = random.choice(list(item_i_76))
                item = item_i_76[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_i))
                item = item_i[item]
                item_loot.append(item)
    elif 95 < d100:
        gem_t = gem_5000[random.randint(1, 4)]
        gem_n = random.randint(1, 8)
        item_n = random.randint(1, 4)
        for _ in itertools.repeat(None, item_n):
            choice = random.randint(1, 100)
            if choice == 76:
                item = random.choice(list(item_i_76))
                item = item_i_76[item]
                item_loot.append(item)
            else:
                item = random.choice(list(item_i))
                item = item_i[item]
                item_loot.append(item)
    else:
        pass
    print(" ")
    print("## Gems, Art, and Items ##")
    print(gem_n, "x ", gem_t)
    for item in item_loot:
        print(item)


def loot_coins_fn():
    global cp
    global sp
    global ep
    global gp
    global pp
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0
    if size in ("I", "i", "Individual", "individual"):
        if cr <= 4:
            d100 = random.randint(1, 100)
            if d100 <= 30:
                for dice in range(5):
                    rolls = random.randint(1.6)
                    cp = cp + rolls
            elif 30 < d100 <= 60:
                for dice in range(4):
                    rolls = random.randint(1, 6)
                    sp = sp + rolls
            elif 60 < d100 <= 70:
                for dice in range(3):
                    rolls = random.randint(1, 6)
                    ep = ep + rolls
            elif 70 < d100 <= 95:
                for dice in range(3):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
            elif 95 < d100:
                pp = random.randint(1, 6)
            else:
                pass
        elif 4 < cr <= 10:
            d100 = random.randint(1, 100)
            if d100 <= 30:
                for dice in range(4):
                    rolls = random.randint(1, 6)
                    cp = cp + rolls
                cp = cp * 100
                for dice in range(6):
                    rolls = random.randint(1, 6)
                    ep = ep + rolls
                ep = ep * 10
            elif 30 < d100 <= 60:
                for dice in range(6):
                    rolls = random.randint(1, 6)
                    sp = sp + rolls
                sp = sp * 10
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
                gp = gp * 10
            elif 60 < d100 <= 70:
                for dice in range(3):
                    rolls = random.randint(1, 6)
                    ep = ep + rolls
                ep = ep * 10
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
                gp = gp * 10
            elif 70 < d100 <= 95:
                for dice in range(4):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
                gp = gp * 10
            elif 95 < d100:
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
                gp = gp * 10
                for dice in range(3):
                    rolls = random.randint(1, 6)
                    pp = pp + rolls
            else:
                pass
        elif 10 < cr < 17:
            d100 = random.randint(1, 100)
            if d100 <= 20:
                for dice in range(4):
                    rolls = random.randint(1, 6)
                    sp = sp + rolls
                sp = sp * 100
                gp = 100 * random.randint(1, 6)
            elif 20 < d100 <= 35:
                ep = random.randint(1, 6) * 100
                gp = random.randint(1, 6) * 100
            elif 35 < d100 <= 75:
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
                gp = gp * 100
            elif 75 < d100:
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
                gp = gp * 100
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    pp = pp + rolls
                pp = pp * 10
            else:
                pass
        elif 17 <= cr:
            d100 = random.randint(1, 100)
            if d100 <= 15:
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    ep = ep + rolls
                ep = ep * 1000
                for dice in range(8):
                    rolls = random.randint(1, 6)
                    gp = gp + rolls
                gp = gp * 100
            elif 15 < d100 <= 55:
                gp = random.randint(1, 6) * 1000
                pp = random.randint(1, 6) * 100
            elif 55 < d100:
                gp = random.randint(1, 6) * 1000
                for dice in range(2):
                    rolls = random.randint(1, 6)
                    pp = pp + rolls
                pp = pp * 100
            else:
                pass
        else:
            loot_coins_fn()
    elif size in ("H", "h", "Hoard", "hoard"):
        if cr <= 4:
            for dice in range(6):
                rolls = random.randint(1, 6)
                cp = cp + rolls
            cp = cp * 100
            for dice in range(3):
                rolls = random.randint(1, 6)
                sp = sp + rolls
            sp = sp * 100
            for dice in range(2):
                rolls = random.randint(1, 6)
                gp = gp * 10
        elif 4 < cr <= 10:
            for dice in range(2):
                rolls = random.randint(1, 6)
                cp = cp + rolls
            cp = cp * 100
            for dice in range(2):
                rolls = random.randint(1, 6)
                sp = sp + rolls
            sp = sp * 1000
            for dice in range(6):
                rolls = random.randint(1, 6)
                gp = gp + rolls
            gp = gp * 100
            for dice in range(3):
                rolls = random.randint(1, 6)
                pp = pp + rolls
            pp = pp * 10
        elif 10 < cr < 17:
            for dice in range(4):
                rolls = random.randint(1, 6)
                gp = gp + rolls
            gp = gp * 1000
            for dice in range(5):
                rolls = random.randint(1, 6)
                pp = pp + rolls
            pp = pp * 100
        elif 17 <= cr:
            for dice in range(12):
                rolls = random.randint(1, 6)
                gp = gp + rolls
            gp = gp * 1000
            for dice in range(8):
                rolls = random.randint(1, 6)
                pp = pp + rolls
            pp = pp * 1000
        else:
            loot_coins_fn()
    else:
        loot_coins_fn()
    print("")
    print("## Coins ##")
    print("cp: ", ep)
    print("sp: ", sp)
    print("ep: ", ep)
    print("gp: ", gp)
    print("pp: ", pp)


def loot_menu_fn():
    print("")
    global cr
    global size
    cr = float(input("Enter CR that loot is being awarded for (e.g.: 0.5, 5, 17): "))
    size = input("Enemies being looted, (I)ndividual or (H)oard? ")
    if size in ("H", "h", "Hoard", "hoard"):
        loot_coins_fn()
        if cr < 5:
            loot_cr1_fn()
        elif 5 <= cr < 11:
            loot_cr5_fn()
        elif 11 <= cr < 17:
            loot_cr11_fn()
        elif 17 < cr:
            loot_cr17_fn()
        else:
            loot_menu_fn()
        start_fn()
    else:
        loot_coins_fn()
        start_fn()


def encounter_fn():
    # player stats
    party_n = int(input("How many players? "))
    if party_n == 1:
        party_lvl = int(input("Enter character level: "))
    elif party_n in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
        party_lvl = int(input("Enter party level SUM: "))
        party_lvl = party_lvl // party_n
    else:
        encounter_fn()
    # monster stats
    mnstr_n = int(input("How many monsters? "))
    if mnstr_n == 1:
        mnstr_cr = int(input("Enter monster CR: "))
    else:
        mnstr_cr = int(input("Enter monster CR SUM: "))
        mnstr_cr = mnstr_cr // mnstr_n
    # party size multipliers
    if party_n in (1, 2):
        if mnstr_n == 1:
            multiplier = 1.5
        elif mnstr_n == 2:
            multiplier = 2
        elif mnstr_n in (3, 4, 5, 6):
            multiplier = 2.5
        elif mnstr_n in (7, 8, 9, 10):
            multiplier = 3
        elif mnstr_n in (11, 12, 13, 14):
            multiplier = 4
        elif mnstr_n >= 15:
            multiplier = 5
        else:
            encounter_fn()
    elif party_n in (3, 4, 5):
        if mnstr_n == 1:
            multiplier = 1
        elif mnstr_n == 2:
            multiplier = 1.5
        elif mnstr_n in (3, 4, 5, 6):
            multiplier = 2
        elif mnstr_n in (7, 8, 9, 10):
            multiplier = 2.5
        elif mnstr_n in (11, 12, 13, 14):
            multiplier = 3
        elif mnstr_n >= 15:
            multiplier = 4
        else:
            encounter_fn()
    elif party_n in (6, 7, 8):
        if mnstr_n == 1:
            multiplier = 0.5
        elif mnstr_n == 2:
            multiplier = 1
        elif mnstr_n in (3, 4, 5, 6):
            multiplier = 1.5
        elif mnstr_n in (7, 8, 9, 10):
            multiplier = 2
        elif mnstr_n in (11, 12, 13, 14):
            multiplier = 2.5
        elif mnstr_n >= 15:
            multiplier = 3
        else:
            encounter_fn()
    else:
        encounter_fn()
    global raw_xp
    global adj_xp
    raw_xp = cr_xp[mnstr_cr]
    adj_xp = raw_xp * multiplier
    if party_lvl == 1:
        if adj_xp >= 100:
            enc_dif = "Deadly"
        elif 100 > adj_xp >= 75:
            enc_dif = "Hard"
        elif 75 > adj_xp >= 50:
            enc_dif = "Medium"
        elif 50 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 2:
        if adj_xp >= 200:
            enc_dif = "Deadly"
        elif 200 > adj_xp >= 150:
            enc_dif = "Hard"
        elif 150 > adj_xp >= 100:
            enc_dif = "Medium"
        elif 100 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 3:
        if adj_xp >= 400:
            enc_dif = "Deadly"
        elif 400 > adj_xp >= 225:
            enc_dif = "Hard"
        elif 225 > adj_xp >= 150:
            enc_dif = "Medium"
        elif 150 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 4:
        if adj_xp >= 500:
            enc_dif = "Deadly"
        elif 500 > adj_xp >= 375:
            enc_dif = "Hard"
        elif 375 > adj_xp >= 250:
            enc_dif = "Medium"
        elif 250 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 5:
        if adj_xp >= 1100:
            enc_dif = "Deadly"
        elif 1100 > adj_xp >= 750:
            enc_dif = "Hard"
        elif 750 > adj_xp >= 500:
            enc_dif = "Medium"
        elif 500 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 6:
        if adj_xp >= 1400:
            enc_dif = "Deadly"
        elif 1400 > adj_xp >= 900:
            enc_dif = "Hard"
        elif 900 > adj_xp >= 600:
            enc_dif = "Medium"
        elif 600 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 7:
        if adj_xp >= 1700:
            enc_dif = "Deadly"
        elif 1700 > adj_xp >= 1100:
            enc_dif = "Hard"
        elif 1100 > adj_xp >= 750:
            enc_dif = "Medium"
        elif 750 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 8:
        if adj_xp >= 2100:
            enc_dif = "Deadly"
        elif 2100 > adj_xp >= 1400:
            enc_dif = "Hard"
        elif 1400 > adj_xp >= 900:
            enc_dif = "Medium"
        elif 900 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 9:
        if adj_xp >= 2400:
            enc_dif = "Deadly"
        elif 2400 > adj_xp >= 1600:
            enc_dif = "Hard"
        elif 1600 > adj_xp >= 1100:
            enc_dif = "Medium"
        elif 1100 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 10:
        if adj_xp >= 2800:
            enc_dif = "Deadly"
        elif 2800 > adj_xp >= 1900:
            enc_dif = "Hard"
        elif 1900 > adj_xp >= 1200:
            enc_dif = "Medium"
        elif 1200 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 11:
        if adj_xp >= 3600:
            enc_dif = "Deadly"
        elif 3600 > adj_xp >= 2400:
            enc_dif = "Hard"
        elif 2400 > adj_xp >= 1600:
            enc_dif = "Medium"
        elif 1600 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 12:
        if adj_xp >= 4500:
            enc_dif = "Deadly"
        elif 4500 > adj_xp >= 3000:
            enc_dif = "Hard"
        elif 3000 > adj_xp >= 2000:
            enc_dif = "Medium"
        elif 2000 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 13:
        if adj_xp >= 5100:
            enc_dif = "Deadly"
        elif 5100 > adj_xp >= 3400:
            enc_dif = "Hard"
        elif 3400 > adj_xp >= 2200:
            enc_dif = "Medium"
        elif 2200 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 14:
        if adj_xp >= 5700:
            enc_dif = "Deadly"
        elif 5700 > adj_xp >= 3800:
            enc_dif = "Hard"
        elif 3800 > adj_xp >= 2500:
            enc_dif = "Medium"
        elif 2500 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 15:
        if adj_xp >= 6400:
            enc_dif = "Deadly"
        elif 6400 > adj_xp >= 4300:
            enc_dif = "Hard"
        elif 4300 > adj_xp >= 2800:
            enc_dif = "Medium"
        elif 2800 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 16:
        if adj_xp >= 7200:
            enc_dif = "Deadly"
        elif 7200 > adj_xp >= 4800:
            enc_dif = "Hard"
        elif 4800 > adj_xp >= 3200:
            enc_dif = "Medium"
        elif 3200 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 17:
        if adj_xp >= 8800:
            enc_dif = "Deadly"
        elif 8800 > adj_xp >= 5900:
            enc_dif = "Hard"
        elif 5900 > adj_xp >= 3900:
            enc_dif = "Medium"
        elif 3900 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 18:
        if adj_xp >= 9500:
            enc_dif = "Deadly"
        elif 9500 > adj_xp >= 6300:
            enc_dif = "Hard"
        elif 6400 > adj_xp >= 4200:
            enc_dif = "Medium"
        elif 4200 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 19:
        if adj_xp >= 10900:
            enc_dif = "Deadly"
        elif 10900 > adj_xp >= 7300:
            enc_dif = "Hard"
        elif 7300 > adj_xp >= 4900:
            enc_dif = "Medium"
        elif 4900 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    elif party_lvl == 20:
        if adj_xp >= 12700:
            enc_dif = "Deadly"
        elif 12700 > adj_xp >= 8500:
            enc_dif = "Hard"
        elif 8500 > adj_xp >= 5700:
            enc_dif = "Medium"
        elif 5700 > adj_xp:
            enc_dif = "Easy"
        else:
            encounter_fn()
    else:
        encounter_fn()
    print("")
    print("Raw XP    : ", raw_xp)
    print("Adjusted XP: ", adj_xp)
    print("Difficulty: ", enc_dif)


def draw_cards_fn():
    global drawn_cards
    drawn_cards = random.sample(card_deck, 5)

    global pos_1
    global pos_2
    global pos_3
    global pos_4
    global pos_5

    pos_1 = random.choice(drawn_cards)
    drawn_cards.remove(pos_1)

    pos_2 = random.choice(drawn_cards)
    drawn_cards.remove(pos_2)

    pos_3 = random.choice(drawn_cards)
    drawn_cards.remove(pos_3)

    pos_4 = random.choice(drawn_cards)
    drawn_cards.remove(pos_4)

    pos_5 = random.choice(drawn_cards)
    drawn_cards.remove(pos_5)


def reveal_cards_fn():
    print("         |--------|")
    print("         |        |")
    print("         | Card 2 |")
    print("         |        |")
    print("|--------|--------|--------|")
    print("|        |        |        |")
    print("| Card 1 | Card 5 | Card 3 |")
    print("|        |        |        |")
    print("|--------|--------|--------|")
    print("         |        |")
    print("         | Card 4 |")
    print("         |        |")
    print("         |--------|")

    print("")
    print("Card 1 - ", pos_1)
    print("The Tome of Strahd (location): This card tells of history.  Knowledge of the ancient will help you better understand your enemy")

    print("")
    print("Card 2 - ", pos_2)
    print("The Holy Symbol of Ravenkind (location):  This card tells of a powerful force for good and protection, a symbol of great hope")

    print("")
    print("Card 3 - ", pos_3)
    print("The Sunsword (location):  This is a card of power and strength.  It tells of a weapon of vengeance:  a sword of sunlight")

    print("")
    print("Card 4 - ", pos_4)
    print("Strahd's Enemy (where to find an ally:  This card sheds light on one who will help you greatly in the battle against darkness")

    print("")
    print("card 5 - ", pos_5)
    print("Strahd (location):  Your enemy is a creature of darkness, whose powers are beyond mortality.  This card will lead you to him")


def wild_magic_fn():
    global roll
    roll = random.randrange(1, 100)
    if roll in (1, 2):
        print("Roll on this table at the start of each of your turns for the next minute, ignoring this result on subsequent rolls")
    elif roll in (3, 4):
        print("For the next minute, you can see any invisible creature if you have line of sight to it")
    elif roll in (5, 6):
        print("A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you, then disappears 1 minute later")
    elif roll in (7, 8):
        print("You cast 'fireball' as 3rd-level spell centered on yourself")
    elif roll in (9, 10):
        print("You cast 'magic missile' as 5th-level spell")
    elif roll in (13, 14):
        print("You cast 'confusion' centered on yourself")
    elif roll in (15, 16):
        print("For the next minute, you regain 5 hit points at the start of each of your turns")
    elif roll in (17, 18):
        print("You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode out from your face")
    elif roll in (19, 20):
        print("You cast 'grease' centered on yourself")
    elif roll in (21, 22):
        print("Creatures have disadvantage on saving throws against the next spell you cast in the next minute that involves a saving throw")
    elif roll in (23, 24):
        print("Your skin turns a vibrant shade of blue.  A 'remove curse' spell can end this effect")
    elif roll in (25, 26):
        print("An eye appears on your forehead for the next minute.  During that time, you have advantage on Wisdom (Perception) checks that rely on sight")
    elif roll in (27, 28):
        print("For the next minute, all your spells with a casting time of 1 action have a casting time of 1 bonus action")
    elif roll in (29, 30):
        print("You teleport up to 60 feet to an unoccupied space of your choice that you can see")
    elif roll in (31, 32):
        print("You are transported to the Astral Plan until the end of your next turn, after which time you return to the space you previously occupied or the nearest unoccupied space if that space is occupied")
    elif roll in (33, 34):
        print("Maximize the damage of the next damaging spell you cast within the next minute")
    elif roll in (41, 42):
        print("You turn into a potted plant until the start of your next turn.  While a plant, you are incapacitated and have vulnerability to all damage.  If you drop to 0 hit points, your pot breaks, and your form revert")
    elif roll in (43, 44):
        print("For the next minute, you can teleport up to 20 feet as a bonus action on each of your turns")
    elif roll in (45, 46):
        print("You cast 'levitate' on yourself")
    elif roll in (47, 48):
        print("A unicorn controlled by the DM appears in a space within 5 feet of you, then disappears 1 minute later")
    elif roll in (49, 50):
        print("You can't speak for the next minute.  Whenever you try, pink bubbles float out of your mouth")
    elif roll in (51, 52):
        print("A spectral shield hovers near you for the next minute, granting you a +2 bonus to AC and immunity to 'magic missile'")
    elif roll in (55, 56):
        print("Your hair falls out but grows back within 24 hours")
    elif roll in (57, 58):
        print("For the next minute, any flammable object you touch that isn't being worn or carried by another creature bursts into flames")
    elif roll in (59, 60):
        print("You regain your lowest-level expended spell slot")
    elif roll in (61, 62):
        print("For the next minute, you must shout when you speak")
    elif roll in (63, 64):
        print("You cast 'fog cloud' centered on yourself")
    elif roll in (67, 68):
        print("You are frightened by the nearest creature until the end of your next turn")
    elif roll in (69, 70):
        print("Each creature within 30 feet of you becomes invisible for the next minute.  The invisibility ends on a creature when it attacks or casts a spell")
    elif roll in (71, 72):
        print("You gain resistance to all damage for the next minute")
    elif roll in (75, 76):
        print("You glow with bright light in a 30-foot radius for the next minute.  Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn")
    elif roll in (77, 78):
        print("You cast 'polymorph' on yourself.  If you fail the saving throw, you turn into a sheep for the spell's duration")
    elif roll in (79, 80):
        print("Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute")
    elif roll in (81, 82):
        print("You can take one additional action immediately")
    elif roll in (85, 86):
        print("You cast 'mirror image'")
    elif roll in (87, 88):
        print("You cast 'fly' on a random creature within 60 feet of you")
    elif roll in (89, 90):
        print("You become invisible for the next minute.  During that time, other creatures can't hear you.  The invisibility ends if you attack or cast a spell")
    elif roll in (91, 92):
        print("If you die within the next minute, you immediately come back to life as if by the 'reincarnate' spell")
    elif roll in (93, 94):
        print("Your size increases by one size category for the next minute")
    elif roll in (95, 96):
        print("You and all creatures within 30 feet of you gain vulnerability to piercing damage for the next minute")
    elif roll in (97, 98):
        print("You are surrounded by faint, ethereal music for the next minute")
    elif roll in (99, 100):
        print("You regain all expended sorcery points")
    elif roll in (11, 12):
        def roll_2_fn():
            roll_2 = random.randint(1, 10)
            if roll_2 in (1, 3, 5, 7, 9):
                print("You shrink ", roll_2, " inches")
            else:
                print("You grow ", roll_2, " inches")
        roll_2_fn()
    elif roll in (35, 36):
        def roll_3_fn():
            roll_3 = random.randint(1, 10)
            if roll_3 in (1, 3, 5, 7, 9):
                print("You grow ", roll_3, " years younger - minimum of one year")
            else:
                print("You grow ", roll_3, " years older")
        roll_3_fn()
    elif roll in (37, 38):
        def roll_4_fn():
            global roll_4
            roll_4 = random.randint(1, 4)
        roll_4_fn()
        print(roll_4, " flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are firghtened of you.  They vanish after 1 minute")

    elif roll in (39, 40):
        def roll_5_fn():
            global roll_5
            roll_5 = random.randint(1, 10)
            roll_5 = (roll_5 * 2)
        roll_5_fn()
        print("You regain ", roll_5, " hit points")
    elif roll in (53, 54):
        def roll_6_fn():
            global days_n
            for _ in itertools.repeat(None, 5):
                days_n = random.randrange(1, 6)
        roll_6_fn()
        print("You are immiune to being intoxicated by alcohol for the next ", days_n, " days")
    elif roll in (65, 66):
        def roll_7_fn():
            global damage
            for _ in itertools.repeat(None, 4):
                damage = random.randint(1, 10)
        roll_7_fn()
        print("Up to three creatures you choose within 30 feet of you take ", damage, " lightning damage")
    elif roll in (73, 74):
        def roll_8_fn():
            global hours
            hours = random.randint(1, 4)
        roll_8_fn()
        print("A random creature within 60 feet of you becomes poisoned for ", hours, " hours")
    elif roll in (83, 84):
        def roll_9_fn():
            global damage
            damage = random.randint(1, 10)
        roll_9_fn()
        print("Each creature within 30 feet of you takes ", damage, " necrotic damage.  You regain hit points equa to the sum damage")
    else:
        pass


def race_fn():
    global char_race
    print("Available Races Include:")
    print("  (R)andom")
    for char_race in race_desc:
        print("  ", char_race)
    char_race = input("Enter Your Race (effects age, height, weight) [R]: ")
    if char_race in race_short:
        pass
    elif char_race in ("R", "r", "Random", "random", ""):
        char_race = (random.choice(race_short))
    else:
        print("Race not available")
        race_fn()


def class_fn():
    def adv_npc_fn():
        adv_npc = input("Select (A)dventurer or (N)PC Class [A]: ")
        if adv_npc in ("A", "a", "Adventurer", "adventurer", ""):
            choose_class()
        elif adv_npc in ("N", "n", "NPC", "npc"):
            choose_class_npc()
        else:
            print("Invalid option")
            adv_npc_fn()
    def choose_class():
        global char_class
        print("Available Classes Include:")
        print("  (R)andom")
        for char_class in class_desc:
            print("  ", char_class)
        char_class = input("Enter Your Class [R]: ")
        if char_class in ("R", "r", "Random", "random", ""):
            char_class = (random.choice(class_short))
        elif char_class not in class_short:
            print("Class not available")
            choose_class()
        else:
            pass
    def choose_class_npc():
        global npc_class
        print("Available Classes Include:")
        print("  (R)andom")
        for npc_class in class_npc:
            print("  ", npc_class)
        npc_class = input("Enter NPC Class [R] ")
        if npc_class in ("R", "r", "Random", "random", ""):
            npc_class = (random.choice(class_npc))
        elif npc_class not in class_npc:
            print("Class not available")
            choose_class_npc()
        global char_class
        char_class = npc_class
    adv_npc_fn()


def height_fn():
    def height_mod_fn():
        global height_mod
        if char_race in ("Dwarf", "Hill Dwarf", "Mountain Dwarf", "Lightfoot Halfling", "Stout Halfling", "Forest Gnome", "Gnome"):
            height_mod = random.randrange(1, 4) + random.randrange(1, 4)
        elif char_race == "Drow":
            height_mod = random.randrange(1, 6) + random.randrange(1, 6)
        elif char_race in ("Dragonborn", "Half-Elf", "Tiefling"):
            height_mod = random.randrange(1, 8) + random.randrange(1, 8)
        elif char_race in ("Human", "High Elf", "Wood Elf", "Elf", "Half-Orc"):
            height_mod = random.randrange(1, 10) + random.randrange(1, 10)
        else:
            pass

    def rnd_height_fn():
        if char_race == "Human":
            height = 56 + height_mod
        elif char_race in ("Dwarf", "Hill Dwarf"):
            height = 44 + height_mod
        elif char_race == "Mountain Dwarf":
            height = 48 + height_mod
        elif char_race in ("Elf", "High Elf", "Wood Elf"):
            height = 54 + height_mod
        elif char_race == "Drow":
            height = 53 + height_mod
        elif char_race in ("Halfling", "Lightfoot Halfling", "Stout Halfling"):
            height = 31 + height_mod
        elif char_race == "Dragonborn":
            height = 66 + height_mod
        elif char_race in ("Gnome", "Forest Gnome"):
            height = 35 + height_mod
        elif char_race in ("Half-Elf", "Tiefling"):
            height = 57 + height_mod
        elif char_race == "Half-Orc":
            height = 58 + height_mod
        else:
            pass
        global char_heightft
        global char_heightin
        char_heightft = math.trunc(height / 12)
        char_heightin = height % 12

    print("Select Character Height:")
    for entry in avg_stats:
        print(entry)
    print("Your race is", char_race)
    height_mod_fn()
    rnd_height = input("Do you want a random height? [Y]: ")
    if rnd_height in ("Y", "y", "Yes", "yes", ""):
        rnd_height_fn()
    elif rnd_height in ("N", "n", "No", "no"):
        height = int(input("Enter your height in total inches: "))
        global char_heightft
        global char_heightin
        char_heightft = math.trunc(height / 12)
        char_heightin = height % 12
    else:
        print(rnd_height, " is not a valid choice")
        height_fn()


def weight_fn():
    def weight_mod_fn():
        global weight_mod
        if char_race in ("Human", "Half-Elf", "Tiefling"):
            weight_mod = height_mod * (random.randrange(1, 4) + random.randrange(1, 4))
        elif char_race in ("Hill Dwarf", "Mountain Dwarf", "Dwarf", "Dragonborn", "Half-Orc"):
            weight_mod = height_mod * (random.randrange(1, 6) + random.randrange(1, 6))
        elif char_race in ("High Elf", "Wood Elf", "Elf"):
            weight_mod = height_mod * random.randrange(1, 4)
        elif char_race == "Drow":
            weight_mod = height_mod * random.randrange(1, 6)
        elif char_race in ("Halfling", "Lightfoot Halfling", "Stout Halfling", "Gnome", "Forest Gnome"):
            weight_mod = height_mod
        else:
            pass

    def rnd_weight_fn():
        global char_weight
        if char_race in ("Human", "Half-Elf", "Tiefling"):
            char_weight = 110 + weight_mod
        if char_race in ("Dwarf", "Hill Dwarf"):
            char_weight = 115 + weight_mod
        if char_race == "Mountain Dwarf":
            char_weight = 130 + weight_mod
        if char_race in ("Elf", "High Elf"):
            char_weight = 90 + weight_mod
        if char_race == "Wood Elf":
            char_weight = 100 + weight_mod
        if char_race == "Drow":
            char_weight = 75 + weight_mod
        if char_race in ("Halfling", "Lightfoot Halfling", "Stout Halfling", "Gnome", "Forest Gnome"):
            char_weight = 35 + weight_mod
        if char_race == "Dragonborn":
            char_weight = 175 + weight_mod
        if char_race == "Half-Orc":
            char_weight = 140 + weight_mod

    print("Select Character Weight:")
    for entry in avg_stats:
        print(entry)
    print("Your race is", char_race)
    weight_mod_fn()
    global rnd_height
    global char_weight
    rnd_weight = input("Do you want a random weight? [Y]: ")
    if rnd_weight in ("Y", "y", "Yes", "yes", ""):
        rnd_weight_fn()
    elif rnd_weight in ("N", "n", "No", "no"):
        char_weight = int(input("Enter your weight in pounds: "))
    else:
        print(rnd_weight, " is not a valid choice")
        weight_fn()


def age_fn():
    global char_age
    for entry in avg_stats:
        print(entry)
    print("Your race is", char_race)
    rnd_age = input("Do you want a random age? [Y]: ")
    if rnd_age in ("Y", "y", "Yes", "yes", ""):
        if char_race in ("Dwarf", "Mountain Dwarf", "Hill Dwarf"):
            char_age = random.randrange(125, 350)
        if char_race in ("Elf", "Wood Elf", "High Elf", "Drow"):
            char_age = random.randrange(175, 750)
        if char_race in ("Halfling", "Lightfoot Halfling", "Stout Halflingl"):
            char_age = random.randrange(50, 150)
        if char_race == "Human":
            char_age = random.randrange(18, 100)
        if char_race == "Dragonborn":
            char_age = random.randrange(18, 100)
        if char_race in ("Gnome", "Forest Gnome"):
            char_age = random.randrange(100, 150)
        if char_race == "Half-Elf":
            char_age = random.randrange(62, 180)
        if char_race == "Half-Orc":
            char_age = random.randrange(30, 80)
        if char_race == "Tiefling":
            char_age = random.randrange(18, 100)
    elif rnd_age in ("N", "n", "No", "no"):
        char_age = int(input("Enter character age: "))
    else:
        print("Not a valid choice")
        age_fn()


def gender_fn():
    global char_gender
    print("Available Genders Include:")
    print("  (R)andom")
    print("  (M)ale")
    print("  (F)emale")
    char_gender = input("Enter character gender [R]: ")
    if char_gender in ("R", "r", "Random", "random", ""):
        char_gender = random.choice("MF")
    if char_gender in ("M", "m", "Male", "male"):
        char_gender = "Male"
    elif char_gender in ("F", "f", "Female", "female"):
        char_gender = "Female"
    else:
        print("Gender not available")
        gender_fn()


def name_fn():
    global char_name
    global plyr_name
    while not plyr_name:
        plyr_name = input("Enter Player Name: ")
    while not char_name:
        char_name = input("Enter Character Name: ")


def abilities_fn():
    def stat_roll():
        d1 = random.randrange(1, 6)
        d2 = random.randrange(1, 6)
        d3 = random.randrange(1, 6)
        d4 = random.randrange(1, 6)
        raw_rolls = [d1, d2, d3, d4]
        sorted_rolls = sorted(raw_rolls)
        del sorted_rolls[0]
        total = sum(sorted_rolls)
        return total

    def strength():
        global abl_str
        abl_str = int(input("Enter the score to use for Strength: "))
        if abl_str not in abl_scores:
            print("Score not valid")
            strength()
        else:
            abl_scores.remove(abl_str)

    def dexterity():
        print("Remaining Scores: ", abl_scores)
        global abl_dex
        abl_dex = int(input("Enter the score to use for Dexterity: "))
        if abl_dex not in abl_scores:
            print("Score not valid")
            dexterity()
        else:
            abl_scores.remove(abl_dex)

    def constitution():
        print("Remaining Scores: ", abl_scores)
        global abl_con
        abl_con = int(input("Enter the score to use for Constitution: "))
        if abl_con not in abl_scores:
            print("Score not valid")
            constitution()
        else:
            abl_scores.remove(abl_con)

    def intelligence():
        print("Remaining Scores: ", abl_scores)
        global abl_int
        abl_int = int(input("Enter the score to use for Intelligence: "))
        if abl_int not in abl_scores:
            print("Score not valid")
            intelligence()
        else:
            abl_scores.remove(abl_int)

    def wisdom():
        print("Remaining Scores: ", abl_scores)
        global abl_wis
        abl_wis = int(input("Enter the score to use for Wisdom: "))
        if abl_wis not in abl_scores:
            print("Score not valid")
            wisdom()
        else:
            abl_scores.remove(abl_wis)

    def charisma():
        print("Remaining Scores: ", abl_scores)
        global abl_cha
        abl_cha = int(input("Enter the score to use for Charisma: "))
        if abl_cha not in abl_scores:
            print("Score not valid")
            charisma()
        else:
            abl_scores.remove(abl_cha)

    def assign():
        rnd_assign = input("Do you want to randomly assign stat rolls? [Y]: ")
        if rnd_assign in ("Y", "y", "Yes", "yes", ""):
            random.shuffle(abl_scores)
            global abl_str
            global abl_dex
            global abl_int
            global abl_con
            global abl_wis
            global abl_cha
            abl_str = random.choice(abl_scores)
            abl_scores.remove(abl_str)
            abl_dex = random.choice(abl_scores)
            abl_scores.remove(abl_dex)
            abl_con = random.choice(abl_scores)
            abl_scores.remove(abl_con)
            abl_int = random.choice(abl_scores)
            abl_scores.remove(abl_int)
            abl_wis = random.choice(abl_scores)
            abl_scores.remove(abl_wis)
            abl_cha = random.choice(abl_scores)
        elif rnd_assign in ("N", "n", "No", "no"):
            strength()
            dexterity()
            constitution()
            intelligence()
            wisdom()
            charisma()
        else:
            print("Invalid choice")
            assign()
    print("Rolling random ability scores...")
    score1 = stat_roll()
    score2 = stat_roll()
    score3 = stat_roll()
    score4 = stat_roll()
    score5 = stat_roll()
    score6 = stat_roll()
    abl_scores = [score1, score2, score3, score4, score5, score6]
    print("  Your Rolles Scores Are: ", abl_scores)
    reroll = input("  Do you want to (C)ontinue or (R)eroll? [C]: ")
    if reroll in ("C", "c", "Continue", "continue", ""):
        assign()
        print("The Scores You Assigned Were:")
        print("   Strength: ", abl_str)
        print("   Dexterity: ", abl_dex)
        print("   Constitution: ", abl_con)
        print("   Intelligence: ", abl_int)
        print("   Wisdom: ", abl_wis)
        print("   Charisma: ", abl_cha)
        choice = input("Do you want to (C)ontinue, Re(A)ssign, or (R)eroll? [C]: ")
        if choice in ("R", "r", "Reroll", "reroll"):
            abilities_fn()
        elif choice in ("A", "a", "Reassign", "reassign", "ReAssign"):
            assign()
        else:
            pass
    else:
        abilities_fn()


def race_bonus_fn():
    global abl_str
    global abl_dex
    global abl_con
    global abl_int
    global abl_wis
    global abl_cha
    print("Specific races give bonuses to certain ability scores.")
    print("The race you selected was: ", char_race, )
    print("Checking for Strength Bonus...")
    if char_race in ("Mountain Dwarf", "Dragonborn", "Half-Orc", "Human"):
        print("   ... you got a bonus!")
        if char_race == "Human":
            abl_str = abl_str + 1
        else:
            abl_str = abl_str + 2
    else:
        pass
    print("Checking for Dexterity Bonus...")
    if char_race in ("Elf", "Wood Elf", "High Elf", "Drow", "Halfling", "Lightfoot Halfling", "Forest Gnome", "Human"):
        print("   ... you got a bonus!")
        if char_race == "Human":
            abl_dex = abl_dex + 1
        else:
            abl_dex = abl_dex + 2
    else:
        pass
    print("Checking for Constitution Bonus...")
    if char_race in ("Dwarf", "Mountain Dwarf", "Hill Dwarf", "Stout Halfling", "Rock Gnome", "Half-Orc", "Human"):
        print("   ... you got a bonus!")
        if char_race in ("Dwarf", "Mountain Dwarf", "Hill Dwarf"):
            abl_con = abl_con + 2
        else:
            abl_con = abl_con + 1
    else:
        pass
    print("Checking for Intelligence Bonus...")
    if char_race in ("High Elf", "Gnome", "Forest Gnome", "Tiefling", "Human"):
        print("   ... you got a bonus!")
        if char_race in ("Gnome", "Forest Gnome"):
            abl_int = abl_int + 2
        else:
            abl_int = abl_int + 1
    else:
        pass
    print("Checking for Wisdom Bonus...")
    if char_race in ("Hill Dwarf", "Wood Elf", "Human"):
        print("   ... you got a bonus!")
        abl_wis = abl_wis + 1
    else:
        pass
    print("Checking for Charisma Bonus...")
    if char_race in ("Half-Elf", "Drow", "Lightfoot Halfling", "Dragonborn", "Human", "Tiefling"):
        print("   ... you got a bonus!")
        if char_race in ("Half-Elf", "Tiefling"):
            abl_cha = abl_cha + 2
        else:
            abl_cha = abl_cha + 2
    else:
        pass


def modifiers_fn():
    global mod_str
    global mod_dex
    global mod_con
    global mod_int
    global mod_wis
    global mod_cha
    global char_ac
    global prim_stat
    global atk_bonus
    print("Each ability score provides a modifier score which benefits certain attributes.")

    def mod(ability):
        if ability == 1:
            mod = -5
            return mod
        elif ability in (2, 3):
            mod = -4
            return mod
        elif ability in (4, 5):
            mod = -3
            return mod
        elif ability in (6, 7):
            mod = -2
            return mod
        elif ability in (8, 9):
            mod = -1
            return mod
        elif ability in (10, 11):
            mod = +0
            return mod
        elif ability in (12, 13):
            mod = 1
            return mod
        elif ability in (14, 15):
            mod = 2
            return mod
        elif ability in (16, 17):
            mod = 3
            return mod
        elif ability in (18, 19):
            mod = 4
            return mod
        elif ability in (20, 21):
            mod = 5
            return mod
        elif ability in (22, 23):
            mod = 6
            return mod
        elif ability in (24, 25):
            mod = 7
            return mod
        elif ability in (26, 27):
            mod = 8
            return mod
        elif ability in (28, 29):
            mod = 9
            return mod
        elif ability == 30:
            mod = 10
            return mod
        else:
            pass
    mod_str = mod(abl_str)
    mod_dex = mod(abl_dex)
    mod_con = mod(abl_con)
    mod_int = mod(abl_int)
    mod_wis = mod(abl_wis)
    mod_cha = mod(abl_cha)
    char_ac = mod_dex + 10
    print("Here are your Ability Scores and (Modifier):")
    print("   Armor Class ", char_ac)
    print("   Strength    ", mod_str)
    print("   Dexterity   ", mod_dex)
    print("   Constitution", mod_con)
    print("   Intelligence", mod_int)
    print("   Wisdom      ", mod_wis)
    print("   Charisma    ", mod_cha)
    print("Each character also gets an attack modifier based on their proficiency bonus + main stat modifier")
    print("The proficiency bonus for Lvl 1 characters is 2")
    print("Your class is: ", char_class)
    print("Calculating attack bonus...")
    if char_class in ("Barbarian"):
        prim_stat = "Strength"
    elif char_class in ("Bard", "Sorcerer", "Warlock"):
        prim_stat = "Charisma"
    elif char_class in ("Cleric", "Druid"):
        prim_stat = "Wisdom"
    elif char_class == "Fighter":
        prim_stat = input("Choose (S)trength, (D)exterity or (R)andom [R]: ")
        if prim_stat in ("R", "r", "Random", "random", ""):
            prim_stat = random.choice("SD")
        if prim_stat in ("S", "s", "Strength", "strength"):
            prim_stat = "Strength"
        elif prim_stat in ("D", "d", "Dexterity", "dexterity"):
            prim_stat = "Dexterity"
        else:
            print("Choice not valid")
            modifiers_fn()
    elif char_class in ("Monk", "Ranger"):
        prim_stat = input("Choose (D)exterity, (W)isdom or (R)andom [R]: ")
        if prim_stat in ("R", "r", "Random", "random", ""):
            prim_stat = random.choice("DW")
        if prim_stat in ("D", "d", "Dexterity", "dexterity"):
            prim_stat = "Dexterity"
        elif prim_stat in ("W", "w", "Wisdom", "wisdom"):
            prim_stat = "Wisdom"
        else:
            print("Choice not valid")
            modifiers_fn()
    elif char_class == "Paladin":
        # str or cha
        prim_stat = input("Choose (S)trength, (C)harisma or (R)andom [R]: ")
        if prim_stat in ("R", "r", "Random", "random", ""):
            prim_stat = random.choice("SC")
        if prim_stat in ("S", "s", "Strength", "strength"):
            prim_stat = "Strength"
        elif prim_stat in ("C", "c", "Charisma", "charisma"):
            prim_stat = "Charisma"
    elif char_class == "Rogue":
        prim_stat = "Dexterity"
    else:
        # Wizard
        prim_stat = "Intelligence"
    if prim_stat == "Strength":
        atk_bonus = mod_str + 2
    if prim_stat == "Dexterity":
        atk_bonus = mod_dex + 2
    if prim_stat == "Intelligence":
        atk_bonus = mod_int + 2
    if prim_stat == "Wisdom":
        atk_bonus = mod_wis + 2
    if prim_stat == "Charisma":
        atk_bonus = mod_cha + 2
    print("Your primary stat is: ", prim_stat)
    print("Your attack bonus is: ", atk_bonus)

def saves_fn():
    print("Calculating saving throw bonuses...")
    # proficiency bonus = 2 for starting characters
    global save_str
    save_str = mod_str
    global save_dex
    save_dex = mod_dex
    global save_con
    save_con = mod_con
    global save_int
    save_int = mod_int
    global save_wis
    save_wis = mod_wis
    global save_cha
    save_cha = mod_cha
    if char_class in ("Barbarian", "barbarian"):
        save_str = save_str + 2
        save_con = save_con + 2
    if char_class in ("Bard", "bard"):
        save_dex = save_dex + 2
        save_cha = save_cha + 2
    if char_class in ("Cleric", "cleric"):
        save_wis = save_wis + 2
        save_cha = save_cha + 2
    if char_class in ("Druid", "druid"):
        save_wis = save_wis + 2
        save_int = save_int + 2
    if char_class in ("Fighter", "fighter"):
        save_str = save_str + 2
        save_con = save_con + 2
    if char_class in ("Monk", "monk"):
        save_str = save_str + 2
        save_dex = save_dex + 2
    if char_class in ("Paladin", "paladin"):
        save_wis = save_wis + 2
        save_cha = save_cha + 2
    if char_class in ("Ranger", "ranger"):
        save_str = save_str + 2
        save_dex = save_dex + 2
    if char_class in ("Rogue", "rogue"):
        save_dex = save_dex + 2
        save_int = save_int + 2
    if char_class in ("Sorcerer", "sorcerer"):
        save_con = save_con + 2
        save_cha = save_cha + 2
    if char_class in ("Warlock", "warlock"):
        save_wis = save_wis + 2
        save_cha = save_cha + 2
    if char_class in ("Wizard", "wizard"):
        save_int = save_int + 2
        save_wis = save_int + 2
    print("   Strength Saves:     ", save_str)
    print("   Dexterity Saves:    ", save_dex)
    print("   Constitution Saves: ", save_con)
    print("   Wisdom Saves:       ", save_wis)
    print("   Intelligence Saves: ", save_int)
    print("   Charisma Saves:     ", save_cha)

def skills_fn():
    print("Some races, and all classes, have a set of skills they are proficient in.")
    global skill_athletics
    skill_athletics = mod_str
    global skill_acrobatics
    skill_acrobatics = mod_dex
    global skill_sleight
    skill_sleight= mod_dex
    global skill_stealth
    skill_stealth = mod_dex
    global skill_arcana
    skill_arcana = mod_dex
    global skill_history
    skill_history = mod_int
    global skill_investigation
    skill_investigation = mod_int
    global skill_nature
    skill_nature = mod_int
    global skill_religion
    skill_religion = mod_int
    global skill_animal
    skill_animal = mod_wis
    global skill_insight
    skill_insight = mod_wis
    global skill_medicine
    skill_medicine = mod_wis
    global skill_perception
    skill_perception = mod_wis
    global skill_survival
    skill_survival = mod_wis
    global skill_deception
    skill_deception = mod_cha
    global skill_intimidation
    skill_intimidation = mod_cha
    global skill_performance
    skill_performance = mod_cha
    global skill_persuasion
    skill_persuasion = mod_cha
    print("   Checking for racial bonus...")
    if char_race in ("Dwarf", "dwarf", "Mountain Dwarf", "mountain dwarf", "Hill Dwarf", "hill dwarf"):
        print("   Your ", char_race, " race has proficiency in History.")
        skill_history = mod_int + 2
    if char_race in ("Elf", "elf", "High Elf", "high elf", "Wood Elf", "wood elf", "Drow", "drow"):
        print("   Your ", char_race, " race has proficiency in Perception.")
        skill_perception = mod_wis + 2
    if char_race in ("Half-Orc", "half-orc"):
        print("   Your ", char_race, " race has proficiency in Intimidation.")
        skill_intimidation = mod_cha + 2
    if char_race in ("Half-Elf", "half-elf"):
        print("   Your ", char_race, " race gives you a choice of skill proficiency.")
        def skill_choice_fn():
            x, y = input("Chose two from: Athletics, Acrobatics, Sleight (of hand), Stealth, Arcana, History, Investigation, Nature, Religion, Animal (handling), Insight, Medicine, Perception, Survival, Deception, Intimidation, Performance, Persuasion, or Random; separated by a space:  ").split()
            if x not in ("Athletics", "Acrobatics", "Sleight", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion", "Animal", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion", "Random", "random", "R", "r"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Athletics", "Acrobatics", "Sleight", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion", "Animal", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion", "Random", "random", "R", "r"):
                print("Invalid input, ", y)
                skill_choice_fn()
            elif x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Athletics":
                skill_athletics = mod_str + 2
            elif x or y == "Acrobatics":
                skill_acrobatics = mod_dex + 2
            elif x or y == "Sleight":
                skill_sleight = mod_dex + 2
            elif x or y == "Stealth":
                skill_stealth = mod_dex + 2
            elif x or y == "Arcana":
                skill_arcana = mod_int + 2
            elif x or y == "History":
                skill_history == mod_int + 2
            elif x or y == "Investigation":
                skill_investigation = mod_int + 2
            elif x or y == "Nature":
                skill_nature = mod_wis + 2
            elif x or y == "Religion":
                skill_religion = mod_wis + 2
            elif x or y == "Animal":
                skill_animal = mod_wis + 2
            elif x or y == "Insight":
                skill_insight = mod_wis + 2
            elif x or y == "Medicine":
                skill_medicine = mod_wis + 2
            elif x or y == "Perception":
                skill_perception = mod_wis + 2
            elif x or y == "Survival":
                skill_survival = mod_wis + 2
            elif x or y == "Deception":
                skill_deception = mod_cha + 2
            elif x or y == "Intimidation":
                skill_intimidation = mod_cha + 2
            elif x or y == "Performance":
                skill_performance = mod_cha + 2
            elif x or y == "Persuasion":
                skill_persuasion = mod_cha + 2
        skill_choice_fn()
    print("   Checking for class bonus...")
    if char_class in ("Bard", "bard"):
        def skill_choice_fn():
            x, y, z = input("Chose three from: Athletics, Acrobatics, Sleight (of hand), Stealth, Arcana, History, Investigation, Nature, Religion, Animal (handling), Insight, Medicine, Perception, Survival, Deception, Intimidation, Performance, Persuasion; separated by a space:  ").split()
            if x not in ("Athletics", "Acrobatics", "Sleight", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion", "Animal", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Athletics", "Acrobatics", "Sleight", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion", "Animal", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if z not in ("Athletics", "Acrobatics", "Sleight", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion", "Animal", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"):
                print("Invalid input", z)
                skill_choice_fn()
            if x in (y, z):
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if y in (x, z):
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y or z == "Athletics":
                skill_athletics = mod_str + 2
            if x or y or z == "Acrobatics":
                skill_acrobatics = mod_dex + 2
            if x or y or z == "Sleight":
                skill_sleight = mod_dex + 2
            if x or y or z == "Stealth":
                skill_stealth = mod_dex + 2
            if x or y or z == "Arcana":
                skill_arcana = mod_int + 2
            if x or y or z == "History":
                skill_history = mod_int + 2
            if x or y or z == "Investigation":
                skill_investigation = mod_int + 2
            if x or y or z == "Nature":
                skill_nature = mod_int + 2
            if x or y or z == "Religion":
                skill_religion = mod_int + 2
            if x or y or z == "Animal":
                skill_religion = mod_wis + 2
            if x or y or z == "Insight":
                skill_insight = mod_wis + 2
            if x or y or z == "Medicine":
                skill_medicine = mod_wis + 2
            if x or y or z == "Perception":
                skill_perception = mod_wis + 2
            if x or y or z == "Survival":
                skill_survival = mod_wis + 2
            if x or y or z == "Deception":
                skill_deception = mod_cha + 2
            if x or y or z == "Intimidation":
                skill_intimidation = mod_cha + 2
            if x or y or z == "Performance":
                skill_performance = mod_cha + 2
            if x or y or z == "Persuasion":
                skill_persuasion = mod_cha + 2
        skill_choice_fn()
    if char_class in ("Barbarian", "barbarian"):
        def skill_choice_fn():
            x, y = input("Chose two from: Animal (handling), Athletics, Intimidation, Nature, Perception, Survival; separated by a space:  ").split()
            if x not in ("Animal", "Athletics", "Intimidation", "Nature", "Perception", "Survival"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Animal", "Athletics", "Intimidation", "Nature", "Perception", "Survival"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Animal":
                skill_animal = mod_wis + 2
            if x or y == "Athletics":
                skill_athletics = mod_str + 2
            if x or y in "Intimidation":
                skill_intimidation = mod_cha + 2
            if x or y in "Nature":
                skill_nature = mod_wis + 2
            if x or y in "Perception":
                skill_perception = mod_wis + 2
            if x or y in "Survival":
                skill_survival = mod_wis + 2
        skill_choice_fn()
    if char_class in ("Cleric", "cleric"):
        def skill_choice_fn():
            x, y = input("Chose two two from: History, Insight, Medicine, Persuasion, Religion; separated by a space:  ").split()
            if x not in ("History", "Insight", "Medicine", "Persuasion", "Religion"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("History", "Insight", "Medicine", "Persuasion", "Religion"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "History":
                skill_history = mod_int + 2
            if x or y == "Insight":
                skill_insight = mod_wis + 2
            if x or y == "Medicine":
                skill_insight = mod_wis + 2
            if x or y == "Persuasion":
                skill_persuasion = mod_cha + 2
            if x or y == "Religion":
                skill_religion = mod_int + 2
        skill_choice_fn()
    if char_class in ("Druid", "druid"):
        def skill_choice_fn():
            x, y = input("Chose two from: Arcana, Animal (handling), Insight, Medicine, Nature, Perception, Religion, Survival; separated by a space:  ").split()
            if x not in ("Arcana", "Animal", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Arcana", "Animal", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Arcana":
                skill_arcana = mod_int + 2
            if x or y == "Insight":
                skill_insight = mod_wis + 2
            if x or y == "Medicine":
                skill_medicine = mod_wis + 2
            if x or y == "Nature":
                skill_nature = mod_int + 2
            if x or y == "Perception":
                skill_peception = mod_wis + 2
            if x or y == "Religion":
                skill_religioin = mod_int + 2
            if x or y == "Survival":
                skill_survival = mod_wis + 2
        skill_choice_fn()
    if char_class in ("Fighter", "fighter"):
        def skill_choice_fn():
            x, y = input("Chose two from: Acrobatics, Animal (handling), Athletics, History, Insight, Intimidation, Perception, Survival; separated by a space:  ").split()
            if x not in ("Acrobatics", "Animal", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Acrobatics", "Animal", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Acrobatics":
                skill_acrobatics = mod_dex + 2
            if x or y == "Animal":
                skill_animal = mod_wis + 2
            if x or y == "Athletics":
                skill_athletics = mod_str + 2
            if x or y == "History":
                skill_history = mod_int + 2
            if x or y == "Insight":
                skill_insight = mod_wis + 2
            if x or y == "Intimidation":
                skill_intimidation = mod_cha + 2
            if x or y == "Perception":
                skill_perception = mod_wis + 2
            if x or y == "Survival":
                skill_survival = mod_wis + 2
        skill_choice_fn()
    if char_class in ("Monk", "monk"):
        def skill_choice_fn():
            x, y = input("Chose two from: Acrobatics, Athletics, History, Insight, Religion, Stealth; separated by a space:  ").split()
            if x not in ("Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Acrobatics":
                skill_acrobatics = mod_dex + 2
            if x or y == "Athletics":
                skill_athletics = mod_str + 2
            if x or y == "History":
                skill_history = mod_int + 2
            if x or y == "Insight":
                skill_insight = mod_wis + 2
            if x or y == "Religion":
                skill_religion = mod_int + 2
            if x or y == "Stealth":
                skill_stealth = mod_dex + 2
        skill_choice_fn()
    if char_class in ("Paladin", "paladin"):
        def skill_choice_fn():
            x, y = input("Choose two from: Athletics, Insight, Intimidation, Medicine, Persuasion, Religion; separated by a space:  ").split()
            if x not in ("Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_chocie_fn()
            if x or y == "Athletics":
                skill_athletics = mod_str + 2
            if x or y == "Insight":
                skill_insight = mod_wis + 2
            if x or y == "Intimidation":
                skill_intimidation = mod_cha + 2
            if x or y == "Medicine":
                skill_medicine = mod_wis + 2
            if x or y == "Persuasion":
                skill_persuasion = mod_cha + 2
            if x or y == "Religion":
                skill_religion = mod_int + 2
        skill_choice_fn()
    if char_class in ("Ranger", "ranger"):
        def skill_choice_fn():
            x, y, z = input("Chose three from: Animal (handling), Athletics, Insight, Investigation, Nature, Perception, Stealth, Survival; separated by a spaces:  ").split()
            if x not in ("Animal", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Animal", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if z not in ("Animal", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x in (y, z):
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if y in (x, z):
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y or z == "Animal":
                skill_animal = mod_wis + 2
            if x or y or z == "Athletics":
                skill_athletics = mod_str + 2
            if x or y or z == "Insight":
                skill_insight = mod_wis + 2
            if x or y or z == "Investigation":
                skill_investigation = mod_int + 2
            if x or y or z == "Nature":
                skill_nature = skill_nature + 2
            if x or y or z == "Perception":
                skill_perception = mod_wis + 2
            if x or y or z == "Stealth":
                skill_stealth = mod_dex + 2
            if x or y or z == "Survival":
                skill_surviavl = mod_wis + 2
        skill_choice_fn()
    if char_class in ("Rogue", "rogue"):
        def skill_choice_fn():
            a, b, c, d = input("Chose four from: Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight (of hand), Stealth; separated by spaces:  ").split()
            if a not in ("Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight", "Stealth"):
                print("Invalid input, ", a)
                skill_choice_fn()
            if b not in ("Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight", "Stealth"):
                print("Invalid input, ", b)
                skill_choice_fn()
            if c not in ("Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight", "Stealth"):
                print("Invalid input, ", c)
                skill_choice_fn()
            if d not in ("Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight", "Stealth"):
                print("Invalid input, ", d)
                skill_choice_fn()
            if a in (b, c, d):
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if b in (a, c, d):
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if c in (a, b, d):
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if a or b or c or d == "Acrobatics":
                skill_acrobatics = mod_dex + 2
            if a or b or c or d == "Athletics":
                skill_athletics = mod_str + 2
            if a or b or c or d == "Deception":
                skill_deception = mod_cha + 2
            if a or b or c or d == "Insight":
                skill_insight = mod_wis + 2
            if a or b or c or d == "Intimidation":
                skill_intimidation = mod_cha + 2
            if a or b or c or d == "Investigation":
                skill_investigation = mod_int + 2
            if a or b or c or d == "Perception":
                skill_perception = mod_wis + 2
            if a or b or c or d == "Performance":
                skill_performance = mod_cha + 2
            if a or b or c or d == "Persuasion":
                skill_persuasion = mod_cha + 2
            if a or b or c or d == "Sleight":
                skill_slieght = mod_dex + 2
            if a or b or c or d == "Stealth":
                skill_stealth = mod_dex + 2
        skill_choice_fn()
    if char_class in ("Sorcerer", "sorcerer"):
        def skill_choice_fn():
            x, y = input("Chose two from: Arcana, Deception, Insight, Intimation, Persuasion, Religion; separated by a space:  ").split()
            if x not in ("Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Arcana":
                skill_arcana = mod_int + 2
            if x or y == "Deception":
                slkill_deception = mod_cha + 2
            if x or y == "Insight":
                skill_insight = mod_wis + 2
            if x or y == "Intimidation":
                skill_intimidation = mod_cha + 2
            if x or y == "Persuasion":
                skill_persuasion = mod_cha + 2
            if x or y == "Religion":
                skill_religion = mod_int + 2
        skill_choice_fn()
    if char_class in ("Warlock", "warlock"):
        def skill_choice_fn():
            x, y = input("Chose two from: Arcana, Deception, History, Intimidation, Investigation, Nature, Religion; separated by a space:  ").split()
            if x not in ("Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Arcana":
                skill_arcana = mod_int + 2
            if x or y == "Deception":
                skill_deception = mod_cha + 2
            if x or y == "History":
                skill_history = mod_int + 2
            if x or y == "Intimidation":
                skill_intimidation = mod_cha + 2
            if x or y == "Investigation":
                skill_investigation = mod_int + 2
            if x or y == "Nature":
                skill_nature = mod_int + 2
            if x or y == "Religion":
                skill_religion = mod_int + 2
        skill_choice_fn()
    if char_class in ("Wizard", "wizard"):
        def skill_choice_fn():
            x, y = input("Chose two from: Arcana, History, Insight, Investigation, Medicine, Religion; separated by a space:  ").split()
            if x not in ("Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"):
                print("Invalid input, ", x)
                skill_choice_fn()
            if y not in ("Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"):
                print("Invalid input, ", y)
                skill_choice_fn()
            if x == y:
                print("You cannot make the same selection twice.")
                skill_choice_fn()
            if x or y == "Arcana":
                skill_arcana = mod_int + 2
            if x or y == "History":
                skill_history = mod_int + 2
            if x or y == "Insight":
                skill_insight = mod_int + 2
            if x or y == "Investigation":
                skill_investigation = mod_int + 2
            if x or y == "Medicine":
                skill_medicine = mod_wis + 2
            if x or y == "Religion":
                skill_religion = mod_int + 2
        skill_choice_fn()

def hp_fn():
    global char_hp
    print("Now we need to calculate hit points.")
    if char_class in ("Barbarian"):
        hit_die = random.randint(1, 12)
        char_hp = mod_con + hit_die
        print("You scored ", char_hp, " hit points")
    elif char_class in ("Fighter", "Paladin", "Ranger"):
        hit_die = random.randint(1, 10)
        char_hp = mod_con + hit_die
        print("You scored ", char_hp, " hit points")
    elif char_class in ("Wizard", "Sorcerer"):
        hit_die = random.randint(1, 6)
        char_hp = mod_con + hit_die
        print("You scored ", char_hp, " hit points")
    else:
        hit_die = random.randint(1, 8)
        char_hp = mod_con + hit_die
        print("You scored ", char_hp, " hit points")


def alignment_fn():
    def lawchaos():
        global align_lawchaos
        align_lawchaos = input("Choose (L)awful, (C)haotic, or (N)eutral: ")
        if align_lawchaos in ("L", "l", "Lawful", "lawful"):
            align_lawchaos = "Lawful"
        elif align_lawchaos in ("C", "c", "Chaotic", "chaotic"):
            align_lawchaos = "Chaotic"
        elif align_lawchaos in ("N", "n", "Neutral", "neutral"):
            align_lawchaos = "Neutral"
        else:
            print("Invalid choice")
            lawchaos()

    def goodevil():
        global align_goodevil
        align_goodevil = input("Choose (G)ood, (E)vil, or (N)eutral: ")
        if align_goodevil in ("G", "g", "Good", "good"):
            align_goodevil = "Good"
        elif align_goodevil in ("E", "e", "Evil", "evil"):
            align_goodevil = "Evil"
        elif align_goodevil in ("N", "n", "Neutral", "neutral"):
            align_goodevil = "Neutral"
        else:
            print("Invalid choice")
            goodevil()

    def cont():
        choice = input("Is this correct? (y/n) ")
        if choice in ("Y", "y", "Yes", "yes"):
            pass
        elif choice in ("N", "n", "No", "no"):
            alignment_fn()
        else:
            cont()

    print("Finally choose alignment.")
    rnd_align = input("Do you want to use a random alignment? [Y]: ")
    if rnd_align in ("Y", "y", "Yes", "yes", ""):
        goodevil_ls = ["Good", "Evil", "Neutral"]
        lawchaos_ls = ["Lawful", "Chaotic", "Neutral"]
        global align_lawchaos
        global align_goodevil
        align_lawchaos = random.choice(lawchaos_ls)
        align_goodevil = random.choice(goodevil_ls)
    elif rnd_align in ("N", "n", "No", "no"):
        lawchaos()
        goodevil()
    else:
        print("Invalid choice")
        alignment_fn()
    print("Your alignment is ", align_lawchaos, "-", align_goodevil)

def summary_fn():
    print("###########################################")
    print("Dungeons and Dragons, 5th Edition Character")
    print("###########################################")
    print("")
    print("GENERAL INFORMATION:")
    if char_name:
        print("Character:      ", char_name)
    print("    Race:           ", char_race)
    print("    Class:          ", char_class)
    if plyr_name:
        print("    Player:         ", plyr_name)
    print("")
    print("    Height:         ", char_heightft, "'", char_heightin, '"')
    print("    Weight:         ", char_weight, "lbs.")
    print("    Age:            ", char_age, "years old")
    print("    Gender:         ", char_gender)
    print("    Alignment:      ", align_lawchaos, "-", align_goodevil)
    print("")
    print("BASIC STATS:")
    print("    Max Hit Points: ", char_hp)
    print("    Armor Class:    ", char_ac)
    print("    Attack Bonus:   ", atk_bonus)
    print("    Primary Stat:   ", prim_stat)
    print("")
    print("ABILITY SCORES:")
    print("    Strength:       ", abl_str, "(", mod_str, ")")
    print("    Dexterity:      ", abl_dex, "(", mod_dex, ")")
    print("    Constitution:   ", abl_con, "(", mod_con, ")")
    print("    Intelligence:   ", abl_int, "(", mod_int, ")")
    print("    Wisdom:         ", abl_wis, "(", mod_wis, ")")
    print("    Charisma:       ", abl_cha, "(", mod_cha, ")")
    print("")
    print("SAVING THROWS:")
    print("    Strength:    ", save_str)
    print("    Dexterity:   ", save_dex)
    print("    Constitution ", save_con)
    print("    Intelligence ", save_int)
    print("    Wisdom:      ", save_wis)
    print("    Charisma:    ", save_cha)
    print("")
    print("SKILLS:")
    print("    Athletics (STR):      ", skill_athletics)
    print("    Acrobatics (DEX)      ", skill_acrobatics)
    print("    Sleight of Hand (DEX) ", skill_sleight)
    print("    Stealth (DEX)         ", skill_stealth)
    print("    Arcana (INT)          ", skill_arcana)
    print("    History (INT)         ", skill_history)
    print("    Investigation (INT)   ", skill_investigation)
    print("    Nature (INT)          ", skill_nature)
    print("    Religion (INT)        ", skill_religion)
    print("    Animal Handling (WIS) ", skill_animal)
    print("    Insight (WIS)         ", skill_insight)
    print("    Medicine (WIS)        ", skill_medicine)
    print("    Perception (WIS)      ", skill_perception)
    print("    Survival (WIS)        ", skill_survival)
    print("    Deception (CHA)       ", skill_deception)
    print("    Intimidation (CHA)    ", skill_intimidation)
    print("    Performance (CHA)     ", skill_performance)
    print("    Persuasion (CHA)      ", skill_persuasion)

def save_fn():
    save_opt = input("Do you want to save this character? [Y]: ")
    if save_opt in ("Y", "y", "Yes", "yes", ""):
        original = sys.stdout
        f = open(char_name + ".txt", "w")
        sys.stdout = f
        summary_fn()
        f.close()
        sys.stdout = original
        start_fn()
    else:
        start_fn()


##########
# Script #
##########

start_fn()
