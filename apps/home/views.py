from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect

from .forms import *
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate
from django.conf import settings


def index(request):
    response = render(request, 'home/index.html', {})
    return response


def rules(request):
    response = render(request, 'home/rules.html', {})
    return response


def about(request):
    response = render(request, 'home/about.html', {})
    return response


def contact(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ContactForm()
        response = render(request, 'home/contact.html', context)

    elif request.method == 'POST':
        back_url = request.META.get('HTTP_REFERER')
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            message = 'Done'
            response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})

        else:
            message = form.errors
            response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})

    else:
        response = render(request, 'home/errors/404.html', {})
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


def logout(request):
    auth_logout(request)
    response = HttpResponseRedirect(reverse('login'))
    return response


def panel(request):
    if request.user.is_authenticated:
        current_user = request.user
        # orders = Order.objects.filter(user_id=current_user)
        profile = Profile.objects.get(user=current_user)

        # found_count = 0
        #
        # for item in orders:
        #     found_count += item.found.all().count()

        response = render(request, 'dashboard/panel.html', {
            'credit': profile.credit,
        })
    else:
        response = render(request, 'dashboard/login.html', {})
    return response


def profile(request):
    current_user = request.user
    back_url = request.META.get('HTTP_REFERER')

    if request.method == 'GET':

        user_profile = Profile.objects.filter(user=current_user).first()
        response = render(request, 'dashboard/profile.html', {
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'email': current_user.email,
        })
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        if check_password(password, current_user.password):
            try:
                Profile.objects.filter(user=current_user).update(
                    phone=phone,
                )

                User.objects.filter(user=current_user).update(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=new_password
                )

                message = 'Done'
                response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})

            except:
                message = 'There is some error'
                response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})
        else:
            message = 'Password is wrong'
            response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})
    else:
        message = 'There is some error'
        response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})

    return response


def page_not_found(request, exception):
    response = render(request, 'home/errors/404.html', {})
    return response


def server_error(request):
    response = render(request, 'home/errors/500.html', {})
    return response


def permission_denied(request, exception):
    response = render(request, 'home/errors/403.html', {})
    return response


def bad_request(request, exception):
    response = render(request, 'home/errors/400.html', {})
    return response
