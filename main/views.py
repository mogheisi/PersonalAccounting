from json import JSONEncoder

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count, Sum
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib import messages
from .form import SignupForm, ExpenseForm, IncomeForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as a_logout
from django.contrib.auth import login as a_login
from .models import Income, Expense, Profile


class IndexPage(TemplateView):
    template_name = 'home/index.html'


def not_login(request):
    return render(request, template_name="home/sign-in.html")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User created")
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(f"{form.errors}")

    form = SignupForm()
    return render(request, "home/sign-up.html", {"form": form})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            a_login(request, user)
            messages.success(request, "Login Successfully")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "wrong username or password")
    form = AuthenticationForm()
    return render(request, "home/sign-in.html", {"form": form})


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        a_logout(request)


@login_required(login_url='../signup/')
def submit_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added')
        return HttpResponse(f"{form.errors}")

    form = ExpenseForm()
    return render(request, 'home/expense.html', {'form': form})


@login_required(login_url='../signup/')
def submit_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added')
        return HttpResponse(f"{form.errors}")
    form = IncomeForm()

    return render(request, 'home/income.html', {'form': form})


@login_required(login_url='../login/')
def view_status(request):
    name = request.user.username
    income = Income.objects.filter(username__username=name).aggregate(Count('amount'), Sum('amount'))
    expense = Expense.objects.filter(username__username=name).aggregate(Count('amount'), Sum('amount'))
    context = {'income': income, 'expense': expense}
    return JsonResponse(context, encoder=JSONEncoder)


