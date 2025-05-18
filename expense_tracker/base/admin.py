from django.contrib import admin
from .models import Year, Months, Budget, Expenses, Categories

# Register your models here.

admin.site.register(Year)
admin.site.register(Months)
admin.site.register(Budget)
admin.site.register(Expenses)
admin.site.register(Categories)