from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Year, Months, Budget, Expenses


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ['year']

class MonthsForm(ModelForm):
    class Meta:
        model = Months
        fields = ['name']

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']
    
class ExpensesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        adjust_type = kwargs.pop("adjust_type", None)
        super().__init__(*args, **kwargs)

        if adjust_type == "add":
            self.fields.pop("category")

    class Meta:
        model = Expenses
        fields = ['expense', 'category']


    
    
