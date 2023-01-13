from django.contrib import messages
from apps.scan.forms import *
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from website.models import *
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from website.forms import LoginForm, RegisterForm, ForgetForm, ContactForm, TicketForm, ProfileForm
from apps.scan.models import *


# back_url = request.META.get('HTTP_REFERER')

def home(request):
    tools_count = Tool.objects.all().count()
    command_count = Command.objects.all().count()
    vulnerability_count = Vulnerability.objects.all().count()
    website_count = Website.objects.all().count()
    fast_scan_form = FastWebsiteScanForm()
    response = render(request, 'home.html', {
        'tools_count': tools_count,
        'command_count': command_count,
        'vulnerability_count': vulnerability_count,
        'website_count': website_count,
        'fast_scan_form': fast_scan_form,
    })
    return response


@login_required(login_url='login')
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    website_list = Website.objects.filter(user=profile.user)
    website_list_complete = website_list.filter(status='COMPLETED')
    website_list_started = website_list.filter(status='STARTED')

    tools = Tool.objects.all()
    commands = Command.objects.all()
    vulnerabilities = Vulnerability.objects.all()

    tools_list = []

    for tool in tools:
        tool_count = commands.filter(tool=tool).count()
        tool_percent = int((100 * tool_count) / commands.count())
        tools_list.append([tool.id, tool.name, tool_count, tool_percent])

    response = render(request, 'dashboard.html', {
        'website_list_all_count': website_list.count(),
        'website_list_complete_count': website_list_complete.count(),
        'website_list_working_count': website_list_started.count(),
        'tools_list': tools_list,
        'vulnerability_list': vulnerabilities,
        'profile': profile,
    })
    return response


@login_required(login_url='login')
def ticket(request):
    form = TicketForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            form.save(request)
            message = 'Done'
            messages.success(request, message)

        else:
            message = form.errors
            messages.error(request, message)

        response = HttpResponseRedirect(reverse('ticket'))

    else:
        tickets = Ticket.objects.filter(user=request.user)
        response = render(request, 'ticket.html', {'form': form, 'tickets': tickets})
    return response


@login_required(login_url='login')
def payment(request):
    payments = Payment.objects.filter(user=request.user)
    response = render(request, 'payment.html', {'payments': payments})
    return response


@login_required(login_url='login')
def profile(request):
    form = ProfileForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            form.update(request)
            message = 'Done'
            messages.success(request, message)

        else:
            message = form.errors
            messages.error(request, message)

        response = HttpResponseRedirect(reverse('profile'))

    else:
        response = render(request, 'profile.html', {'form': form})
    return response


def terms(request):
    response = render(request, 'terms.html', {})
    return response


def privacy(request):
    response = render(request, 'privacy.html', {})
    return response


def about(request):
    response = render(request, 'about.html', {})
    return response


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            message = 'Done'
            messages.success(request, message)

        else:
            message = form.errors
            messages.error(request, message)

        response = HttpResponseRedirect(reverse('profile'))
    else:
        form = ContactForm(request.POST)
        response = render(request, 'contact.html', {'form': form})

    return response


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                message = 'Welcome Back'
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True
                messages.success(request, message)
                response = HttpResponseRedirect(reverse('dashboard'))
            else:
                message = 'Username Or Password Is Wrong'
                messages.error(request, message)
                response = HttpResponseRedirect(reverse('login'))
        else:
            message = form.errors
            messages.error(request, message)
            response = HttpResponseRedirect(reverse('login'))

    else:
        if request.user.is_authenticated:
            response = HttpResponseRedirect(reverse('dashboard'))
        else:
            form = LoginForm()
            response = render(request, 'login.html', {'form': form})
    return response


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            user_exist = User.objects.filter(username=username)

            if not user_exist:
                user = form.save(request)
                auth_login(request, user)
                message = 'Wellcome To Dionaea'
                messages.success(request, message)
                response = HttpResponseRedirect(reverse('dashboard'))

            else:
                message = 'User Is Exist'
                messages.error(request, message)
                response = HttpResponseRedirect(reverse('register'))

        else:
            message = form.errors
            messages.error(request, message)
            response = render(request, 'register.html', {
                'form': form,
            })
    else:
        if request.user.is_authenticated:
            response = HttpResponseRedirect(reverse('dashboard'))
        else:
            form = RegisterForm()
            response = render(request, 'register.html', {'form': form})
    return response


def forget(request):
    form = ForgetForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email=email)

            if not user:
                message = 'User Not Found'
                messages.error(request, message)
                response = HttpResponseRedirect(reverse('forget'))
            else:
                message = 'Rest Password Email Send'
                messages.success(request, message)
                response = HttpResponseRedirect(reverse('forget'))

        else:
            message = form.errors
            messages.error(request, message)
            response = HttpResponseRedirect(reverse('forget'))
    else:
        if request.user.is_authenticated:
            response = HttpResponseRedirect(reverse('dashboard'))
        else:

            response = render(request, 'forget.html', {'form': form})

    return response


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    message = 'You Have Successfully logged Out'
    messages.success(request, message)
    response = HttpResponseRedirect(reverse('login'))
    return response


def page_not_found(request, exception):
    response = render(request, 'errors/404.html', {})
    return response


def server_error(request):
    response = render(request, 'errors/500.html', {})
    return response


def permission_denied(request, exception):
    response = render(request, 'errors/403.html', {})
    return response


def bad_request(request, exception):
    response = render(request, 'errors/400.html', {})
    return response
