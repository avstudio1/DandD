from django.urls import path, include
from django.contrib import admin
import DandD.views
admin.autodiscover()

# Djando style url patterning for navigating through the site 
urlpatterns = [
    path("", DandD.views.index, name="index"),
    path("DandD/currency/", DandD.views.currency, name="currency"),
]

