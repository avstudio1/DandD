from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import game.views

urlpatterns = [
    path("", game.views.index, name="index"),
    path("admin/", admin.site.urls),
]
