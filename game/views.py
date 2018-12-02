from django.shortcuts import render
from game.economy import currency

# Create your views here.
def index(request):
    return render(request, "index.html")

def player(request, player_code):
    player = player_code
    player_account = currency.create_purse(player)
    return render(request, "player.html", {'player': player, 'player_account': player_account})

def economy(request, player):
    purse_owner = player
    purse = currency.create_purse(purse_owner)
    return render(request, "economy.html", {'purse': purse})