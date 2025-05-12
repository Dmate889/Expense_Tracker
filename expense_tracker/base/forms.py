from django.forms import ModelForm
from .models import Year, Months


class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ['year', 'user']

class MonthsForm(ModelForm):
    class Meta:
        model = Months
        fields = ['name', 'created_by']