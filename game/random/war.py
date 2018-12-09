import random

class deck:

    cards = {2 : 'Two',
             3 : 'Three',
             4 : 'Four',
             5 : 'Five',
             6 : 'Six',
             7 : 'Seven',
             8 : 'Eight',
             9 : 'Nine',
             10 : 'Ten',
             11 : 'Jack',
             12 : 'Queen',
             13 : 'King',
             14 : 'Ace'
            }

    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    def __init__(self, cards, suits):
        pass
        
    def create_deck(self):
        new_deck = {}
        for suit in self.suits:
            for value, card in self.cards.items():
                card_name = card + ' of ' + suit
                new_deck[card_name] = value
        return new_deck

def shuffle_deck(card_deck):
    card_list = []
    for card_key in card_deck:
        card_list.append(card_key)
        random.shuffle(card_list)
    return card_list

def normal_round(deck_player_1, deck_player_2):
    # Print round number here???
    round_tally = {'winner' : 0, 'value' : 0}
    flip_player_1 = deck_player_1.pop()
    flip_player_2 = deck_player_2.pop()
    print('Player 1 flips a ' + flip_player_1 + ' (' + str(master_deck.get(flip_player_1)) + ')')
    print('Player 2 flips a ' + flip_player_2 + ' (' + str(master_deck.get(flip_player_2)) + ')')
    if master_deck.get(flip_player_1) > master_deck.get(flip_player_2):
        round_tally['winner'] = 1
        round_tally['value'] = 2
    elif master_deck.get(flip_player_1) < master_deck.get(flip_player_2):
        round_tally['winner'] = 2
        round_tally['value'] = 2
    else:
        #Function call to calculate War goes here
        round_tally['winner'] = 3
        round_tally['value'] = 6
    return round_tally

def war_round(deck_player_1, deck_player_2, score):
    for i in range(2):
        print(i+1, ' cards down.')
        deck_player_1.pop()
        deck_player_2.pop()
    update_score(deck_player_1, deck_player_2, score, 6)

# Execute a card flip and update the score
def update_score(deck_player_1, deck_player_2, score, war_value):
    war = war_value
    round_winner = normal_round(deck_player_1, deck_player_2)
    if round_winner['winner'] == 1:
        print(name_player_1 + ' wins round.')
        score[name_player_1] = score[name_player_1] + (war + round_winner['value'])
    elif round_winner['winner'] == 2:
        print(name_player_2 + ' wins round.')
        score[name_player_2] = score[name_player_2] + (war + round_winner['value'])
    else:
        print('War!')

        war_round(deck_player_1, deck_player_2, score)
    return score

# Setup code runs upon startup
# Creates a score for each player
score_player_1 = 0
score_player_2 = 0

# Create a new master deck of cards and then shuffle them
new_deck_primer = deck(deck.cards, deck.suits)
master_deck = new_deck_primer.create_deck()
shuffled_deck = shuffle_deck(master_deck)

# Allocates half the cards to player 1 and the other half to player 2
deck_player_1 = [i for x,i in enumerate(shuffled_deck) if x%2==1]
deck_player_2 = [i for x,i in enumerate(shuffled_deck) if x%2==0]

# Gets the players names
name_player_1 = input('Enter player one name: ')
name_player_2 = input('Enter player two name: ')

# Create a score dict
score = {name_player_1: score_player_1, name_player_2: score_player_2}
print('Score cards:', score)

def flip():
    update_score(deck_player_1, deck_player_2, score, 0)
    print(score)


