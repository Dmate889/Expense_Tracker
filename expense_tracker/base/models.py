from django.db import models
from django.contrib.auth.models import User
from django.db.models import DecimalField, CharField


# Create your models here.

class Year(models.Model):
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.year)

class Months(models.Model):
    MONTH_CHOICES = [
        ("jan", "January"),
        ("feb", "February"),
        ("mar", "March"),
        ("apr", "April"),
        ("may", "May"),
        ("jun", "June"),
        ("jul", "July"),
        ("aug", "August"),
        ("sep", "September"),
        ("oct", "October"),
        ("nov", "November"),
        ("dec", "December"),
    ]

    name = models.CharField(max_length=3, choices=MONTH_CHOICES)


    year = models.ForeignKey(Year, on_delete= models.CASCADE)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return dict(self.MONTH_CHOICES).get(self.name, self.name)

class Budget(models.Model):
    month = models.OneToOneField(Months, related_name='budget', blank=True, on_delete = models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

class Expenses(models.Model):
    budget =  models.ForeignKey(Budget, null=True, on_delete=models.CASCADE)
    expense = DecimalField(max_digits=10, decimal_places=2)
    category = CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category}: {self.expense}"

