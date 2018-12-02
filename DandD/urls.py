from django.urls import path, include
from django.contrib import admin
import game.views

admin.autodiscover()

urlpatterns = [
    path("", game.views.index, name="index"),
    path("economy/", game.views.economy, name="economy"),
    path("economy/<str:player_code>/", game.views.player, name="player")
]
