from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expense, Income, Profile


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        username = super().save(commit=commit)
        Profile.objects.create(username=username)
        return username


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('username', 'amount', 'date', 'description')


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('username', 'amount', 'date', 'description')

