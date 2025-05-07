from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("getyears/", views.getYears, name="getyears"),
    path("getmonths/", views.getMonths, name="getmonths")
]