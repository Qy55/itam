from django.urls import path

from . import views

urlpatterns = [
    path("assets/",  views.asset_manage,    name="asset_manage"),
]
