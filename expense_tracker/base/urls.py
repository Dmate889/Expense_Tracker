from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("getyears/", views.getYears, name="getyears"),
    path("createyear/", views.createNewYear, name="createyear"),
    path("getmonths/", views.getMonths, name="getmonths"),
    path("createmonth/", views.createMonth, name="createmonth"),
    path('monthexpense/<int:month_id>', views.monthExpense, name="monthexpense"),
]