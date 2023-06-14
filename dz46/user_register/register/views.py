from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RegisterForm
from .models import Register
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'register/home.html')


def sign_up_user(request):
    if request.method == 'GET':
        return render(request, 'register/sign_up_user.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('actual_discount')
            except IntegrityError:
                return render(request, 'register/sign_up_user.html',
                              {'form': UserCreationForm(), 'error': 'Такое имя пользователя уже существует'})
        else:
            return render(request, 'register/sign_up_user.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


@login_required
def actual_discount(request):
    return render(request, 'register/actual_discount.html')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'register/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'register/login_user.html',
                          {'form': AuthenticationForm(), 'error': 'Введены неверные данные'})
        else:
            login(request, user)
            return redirect('actual_discount')


@login_required
def clubadmin(request):
    if request.method == 'GET':
        return render(request, 'register/clubadmin.html', {'form': RegisterForm()})
    else:
        try:
            form = RegisterForm(request.POST)
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('clubadmin')
        except ValueError:
            return render(request, 'register/clubadmin.html',
                          {'form': RegisterForm(),
                           'error': 'Переданы неверные данные. Попробуйте еще раз'
                           })


@login_required
def clublist(request):
    items = Register.objects.all()
    return render(request, 'register/clublist.html', {'items': items})
