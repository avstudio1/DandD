# Base Character class for dd clone '''
# base_character.py

class base_character:
    races=['human',
            'dwarf',
            'elf',
            'hafling',
            'orc',
            'troll',
            'imp',
            'gollum'
            ]
    classes=['wizard',
            'monk',
            'fighter'
            'shield'
            ]

    def __init__(self, char_race, char_class):
        self.char_race = char_race
        self.char_class = char_class

    def getChar(self):
        return "You are a " + self.char_race + " " + self.char_class
