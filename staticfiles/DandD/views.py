import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def dashboard(request):
    return render(request, "index.html")

def airport(request):
    airport = "JFK"
    return render(request, "airport.html", {"airport": airport})

def terminal(request):
    terminal = 0
    return render(request, "terminal.html", {"terminal": terminal})

def stand(request):
    stand = 0
    return render(request, "stand.html", {"stand": stand})
