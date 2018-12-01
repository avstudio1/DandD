import os
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Main index view
def index(request):
    return render(request, "index.html")

# Currency page view
def currency(request):
    return render(request, "currency.html")
