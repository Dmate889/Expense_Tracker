from django.contrib import admin
from .models import Year, Months, Budget, Expenses

# Register your models here.

admin.site.register(Year)
admin.site.register(Months)
admin.site.register(Budget)
admin.site.register(Expenses)