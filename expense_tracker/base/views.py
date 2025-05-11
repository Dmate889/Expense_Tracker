from django.shortcuts import render, redirect
from .models import Months, Year, Budget
from .forms import YearForm, MonthsForm

# Create your views here.

def home(request):
    user = request.user
    return render(request, 'base/home.html', {'user': user})

def getYears(request):
    years = Year.objects.all()
    
    context = {'years': years}
    return render(request, 'base/getyears.html', context)

def createNewYear(request):
    form = YearForm()
    if request.method == "POST":
        form = YearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("getyears")

    context = {"form": form}
    
    return render(request, 'base/createyear.html', context)

def createMonth(request):
    form = MonthsForm()
    if request.method == "POST":
        form = MonthsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("getmonths")

    context = {"form": form}
    
    return render(request, 'base/createmonth.html', context)


def getMonths(request):
    months = Months.objects.all()
    
    context = {'months': months}
    return render(request, 'base/getmonths.html', context)

def monthExpense(request, month_id):
    month = Months.objects.get(id = month_id)
    budget = Budget.objects.get(month = month)


    context = {'budget': budget, 'month': month}
    return render(request, 'base/monthexpense.html', context)