from django.shortcuts import render, redirect, get_object_or_404
from .models import Months, Year, Budget, Expenses
from .forms import YearForm, MonthsForm, BudgetForm, ExpensesForm
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required(login_url='loginpage')
def home(request):
    user = request.user
    return render(request, 'base/home.html', {'user': user})

@login_required(login_url='loginpage')
def getYears(request):
    years = Year.objects.all()
    
    context = {'years': years}
    return render(request, 'base/getyears.html', context)

@login_required(login_url='loginpage')
def getMonths(request, year_id):
    year = get_object_or_404(Year, id=year_id)
    months = Months.objects.filter(year_id=year_id)
    
    context = {'months': months, "year": year}
    return render(request, 'base/getmonths.html', context)

@login_required(login_url='loginpage')
def createNewYear(request):
    form = YearForm()
    if request.method == "POST":
        form = YearForm(request.POST)
        if form.is_valid():
            year =  form.save(commit = False)
            if Year.objects.filter(year = year.year):
                messages.error(request, "This year already exists!")
            else:     
                year.user = request.user
                year.save()
                return redirect("getyears")

    context = {"form": form}
    
    return render(request, 'base/createyear.html', context)

@login_required(login_url='loginpage')
def createMonth(request, year_id):
    year = get_object_or_404(Year, id=year_id)
    form = MonthsForm()

    if request.method == "POST":
        form = MonthsForm(request.POST)
        if form.is_valid():
            month = form.save(commit=False)
            month.year = year
            month.created_by = request.user
            exists = Months.objects.filter(name = month.name, year = month.year).exists()
            if exists:
                messages.error(request, "This month already exists in this year") 
            else:
                month.save()
                return redirect("getmonths", year_id=month.year.id)

    context = {"form": form, "year": year}
    
    return render(request, 'base/createmonth.html', context)


@login_required(login_url='loginpage')
def deleteYear(request, year_id):
    year = get_object_or_404(Year, id = year_id)

    if request.method == "POST":
        year.delete()
        return redirect("home")
    
    return render(request, "base/delete_item.html", {"obj": year})

@login_required(login_url='loginpage')
def deleteMonth(request, month_id):

    month = get_object_or_404(Months, id = month_id)

    if request.method == "POST":
        month.delete()
        return redirect("getmonths", year_id=month.year.id)

    context = {"obj": month}
    return render(request, 'base/delete_item.html', context)

@login_required(login_url='loginpage')
def monthExpense(request, month_id):
    month = get_object_or_404(Months, id = month_id)
    year = month.year
    
    try:
        budget = Budget.objects.get(month = month)
    except: 
        budget = None


    context = {'budget': budget, 'month': month, 'year': year}
    return render(request, 'base/monthexpense.html', context)

@login_required(login_url='loginpage')
def createBudget(request, month_id):

    month = get_object_or_404(Months, id = month_id)
    form = BudgetForm()

    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit = False)
            budget.month = month
            budget.created_by = request.user
            budget.save()
            return redirect("monthexpense", month_id = budget.month.id)

    context = {"form": form, "month": month}

    return render(request, 'base/createBudget.html', context)

@login_required(login_url='loginpage')
def adjustBudget(request, budget_id):
    adjust = request.GET.get("adjust")
    
    form = ExpensesForm(adjust_type = adjust)
    
    budget = get_object_or_404(Budget, id = budget_id)

    if request.method == "POST":
        form = ExpensesForm(request.POST)
        if form.is_valid():
            expense = form.save(commit = False)
            expense.budget = budget
            expense.adjust_type = adjust
            expense.created_by = request.user
            expense.save()
            if adjust == "deduct":
                budget.amount -= expense.expense
                if budget.amount < 0: budget.amount = 0
            elif adjust == "add":
                budget.amount += expense.expense
            
            budget.save()
            return redirect("monthexpense", month_id=expense.budget.month.id)


    context = {"form": form, "budget": budget, "adjust": adjust}
    return render(request, 'base/adjust_amount.html', context)

@login_required(login_url='loginpage')
def listExpenses(request,  budget_id):
    budget = get_object_or_404(Budget, id = budget_id)

    category_amount_sum = Expenses.objects.filter(budget__id = budget_id, adjust_type = "deduct") \
    .values("category__name") \
    .annotate(total = Sum("expense"))
    

    context = {"category_amount_sum": category_amount_sum, "budget": budget}

    return render(request, 'base/list_expenses.html', context)

def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try: 
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User doesn't exists")

        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password is not correct")
    
    return render(request, 'base/login_page.html')



def logout_user(request):

    logout(request)
    return redirect('home')


def register_user(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user =  form.save(commit = False)
           user.save()    
           login(request, user)  
           return redirect("home") 
        else: 
            messages.error(request, "User already exists!")
            
    context = {"form": form}
    return render(request, 'base/register_page.html', context)