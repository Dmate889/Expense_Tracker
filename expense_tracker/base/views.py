from django.shortcuts import render, redirect, get_object_or_404
from .models import Months, Year, Budget
from .forms import YearForm, MonthsForm, BudgetForm, ExpensesForm
from django.contrib import messages

# Create your views here.

def home(request):
    user = request.user
    return render(request, 'base/home.html', {'user': user})

def getYears(request):
    years = Year.objects.all()
    
    context = {'years': years}
    return render(request, 'base/getyears.html', context)

def getMonths(request, year_id):
    year = get_object_or_404(Year, id=year_id)
    months = Months.objects.filter(year_id=year_id)
    
    context = {'months': months, "year": year}
    return render(request, 'base/getmonths.html', context)

def createNewYear(request):
    form = YearForm()
    if request.method == "POST":
        form = YearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("getyears")

    context = {"form": form}
    
    return render(request, 'base/createyear.html', context)

def createMonth(request, year_id):
    year = get_object_or_404(Year, id=year_id)
    form = MonthsForm()

    if request.method == "POST":
        form = MonthsForm(request.POST)
        if form.is_valid():
            month = form.save(commit=False)
            month.year = year
            exists = Months.objects.filter(name = month.name, year = month.year).exists()
            if exists:
                messages.error(request, "This month already exists in this year") 
            else:
                month.save()
                return redirect("getmonths", year_id=month.year.id)

    context = {"form": form, "year": year}
    
    return render(request, 'base/createmonth.html', context)

def deleteYear(request, year_id):
    year = get_object_or_404(Year, id = year_id)

    if request.method == "POST":
        year.delete()
        return redirect("home")
    
    return render(request, "base/delete_item.html", {"obj": year})

def deleteMonth(request, month_id):

    month = get_object_or_404(Months, id = month_id)

    if request.method == "POST":
        month.delete()
        return redirect("getmonths", year_id=month.year.id)

    context = {"obj": month}
    return render(request, 'base/delete_item.html', context)

def monthExpense(request, month_id):
    month = get_object_or_404(Months, id = month_id)
    year = month.year
    
    try:
        budget = Budget.objects.get(month = month)
    except: 
        budget = None


    context = {'budget': budget, 'month': month, 'year': year}
    return render(request, 'base/monthexpense.html', context)

def createBudget(request, month_id):

    month = get_object_or_404(Months, id = month_id)
    form = BudgetForm()

    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit = False)
            budget.month = month
            budget.save()
            return redirect("monthexpense", month_id = budget.month.id)

    context = {"form": form, "month": month}

    return render(request, 'base/createBudget.html', context)

def adjustBudget(request):

    form = ExpensesForm()

    if request.method == "POST":
        form = ExpensesForm(request.POST)
        


    context = {}
    return render(request, 'base/adjust_amount.html', context)