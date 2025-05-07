from django.shortcuts import render
from .models import Months, Year

# Create your views here.

def home(request):
    user = request.user
    return render(request, 'base/home.html', {'user': user})

def getYears(request):
    years = Year.objects.all
    
    context = {'years': years}
    return render(request, 'base/getyears.html', context)


def getMonths(request):
    months = Months.objects.all
    
    context = {'months': months}
    return render(request, 'base/getmonths.html', context)