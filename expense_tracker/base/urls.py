from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("getyears/", views.getYears, name="getyears"),
    path("createyear/", views.createNewYear, name="createyear"),
    path("getmonths<int:year_id>/", views.getMonths, name="getmonths"),
    path("createmonth/<int:year_id>", views.createMonth, name="createmonth"),
    path('monthexpense/<int:month_id>', views.monthExpense, name="monthexpense"),
]