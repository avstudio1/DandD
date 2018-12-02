# base_character.py
# Updated 2018-12-01
# Justin Wood

class base_character:

    races=['human',
           'dwarf',
           'elf',
           'hafling',
           'orc',
           'troll',
           'imp',
           'gollum',
           ]

    classes=['wizard',
             'monk',
             'fighter'
             'shield',
             'cleric',
             'bard',
             'thief',
             'assasin',
             ]

    def __init__(self, char_race, char_class):
        self.char_race = char_race
        self.char_class = char_class

    def getChar(self):
        return "You are a " + self.char_race + " " + self.char_class
