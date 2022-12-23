from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apps.dashboard.models import *
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from apps.home.forms import LoginForm, RegisterForm, ForgetForm
from apps.scan.models import *


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        current_user = request.user
        orders = Scan.objects.filter(user_id=current_user)
        profile = Profile.objects.get(user=current_user)
        complete = Scan.objects.filter(percent='100', user_id=current_user)

        found_count = 0

        for item in orders:
            found_count += item.found.all().count()

        response = render(request, 'dashboard/index.html', {
            'order_count': orders.count(),
            'found_count': found_count,
            'complete_count': complete.count(),
            'credit': profile.credit,
        })
    else:
        response = render(request, 'dashboard/login.html', {})
    return response


def login(request):
    back_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                response = HttpResponseRedirect(reverse('dashboard'))
            else:
                message = 'Username Or Password Is Wrong'
                response = render(request, 'dashboard/message.html', {'message': message, 'back_url': back_url})
        else:
            message = form.errors
            response = render(request, 'dashboard/message.html', {'message': message, 'back_url': back_url})

    else:
        if request.user.is_authenticated:
            response = HttpResponseRedirect(reverse('dashboard'))
        else:
            context = {}
            context['form'] = LoginForm()
            response = render(request, 'dashboard/login.html', context)
    return response


def register(request):
    back_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user_exist = User.objects.filter(username=username)
            email_exist = User.objects.filter(email=email)

            if not user_exist and not email_exist:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                auth_login(request, user)
                response = HttpResponseRedirect(reverse('dashboard'))

            else:
                message = 'User Is Exist'
                response = render(request, 'dashboard/message.html', {'message': message, 'back_url': back_url})

        else:
            message = form.errors
            response = render(request, 'dashboard/message.html', {'message': message, 'back_url': back_url})
    else:
        if request.user.is_authenticated:
            response = HttpResponseRedirect(reverse('dashboard'))
        else:
            context = {}
            context['form'] = RegisterForm()
            response = render(request, 'dashboard/register.html', context)
    return response


def forget_password(request):
    back_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ForgetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email=email)

            if not user:
                message = 'User Not Found'
                response = render(request, 'dashboard/message.html', {'message': message, 'back_url': back_url})
            else:
                message = 'Done'
                response = render(request, 'dashboard/message.html', {'message': message, 'back_url': back_url})

        else:
            message = form.errors
            response = render(request, 'dashboard/message.html', {'message': message, 'back_url': back_url})
    else:
        if request.user.is_authenticated:
            response = HttpResponseRedirect(reverse('dashboard'))
        else:
            context = {}
            context['form'] = ForgetForm()
            response = render(request, 'dashboard/forget_password.html', context)

    return response


def profile(request):
    response = render(request, 'dashboard/profile.html', {})
    return response


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        response = render(request, 'dashboard/login.html', {})
    else:
        response = render(request, 'dashboard/login.html', {})
    return response
