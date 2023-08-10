from django.urls import path

from . import views

urlpatterns = [
    # path("assets/",  views.asset_manage,    name="asset_manage"),
    path("assets/",  views.AssetManage.as_view(),    name="asset_manage"),
]
