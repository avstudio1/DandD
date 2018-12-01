from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import customer.views

# Tiered url patterning for navigating through different airports 
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path("", customer.views.index, name="index"),
    path("contact/", customer.views.contact, name="contact"),
    path("contact/thanks/", customer.views.thanks, name="thanks"),
    path("airport/", customer.views.customers, name="customers"),
    path("airport/<str:airportcode>/", customer.views.airport, name="airport"),
    path("airport/<str:airportcode>/<str:terminalcode>/", customer.views.terminal, name="terminal"),
    path("airport/<str:airportcode>/<str:terminalcode>/<str:standcode>", customer.views.stand, name="stand"),
    path("admin/", admin.site.urls),
]

