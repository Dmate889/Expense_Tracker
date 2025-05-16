from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("getyears/", views.getYears, name="getyears"),
    path("createyear/", views.createNewYear, name="createyear"),
    path("deleteyear/<int:year_id>", views.deleteYear, name="deleteyear"),
    path("deletemonth/<int:month_id>", views.deleteMonth, name="deletemonth"),
    path("getmonths<int:year_id>/", views.getMonths, name="getmonths"),
    path("createmonth/<int:year_id>", views.createMonth, name="createmonth"),
    path('monthexpense/<int:month_id>', views.monthExpense, name="monthexpense"),
    path('createbudget/<int:month_id>', views.createBudget, name="createbudget"),
    path('adjust_amount/<int:budget_id>', views.adjustBudget, name="adjustamount"),
]