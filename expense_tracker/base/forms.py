from django.forms import ModelForm
from .models import Year, Months, Budget, Expenses


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ['year', 'user']

class MonthsForm(ModelForm):
    class Meta:
        model = Months
        fields = ['name', 'created_by']

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'created_by']
    
class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'