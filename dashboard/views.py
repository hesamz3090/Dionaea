from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from dashboard.models import *
import re
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from urllib.parse import urlsplit
from scan.models import *


def index(request):
    if request.user.is_authenticated:
        current_user = request.user
        orders = Order.objects.filter(user_id=current_user)
        profile = Profile.objects.get(user=current_user)
        complete = Order.objects.filter(percent='100', user_id=current_user)

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


@login_required(login_url='login')
def scan(request):
    if request.method == 'POST':
        current_user = request.user

        def url_maker(url):
            if not re.match(r'http(s?)\:', url):
                url = 'http://' + url
            parsed = urlsplit(url)
            host = parsed.netloc
            if host.startswith('www.'):
                host = host[4:]
            return host

        address = url_maker(request.POST['address'])
        panel_type = request.POST['type']
        profile = Profile.objects.get(user=current_user)

        if panel_type == 'simple':
            plan = request.POST['plan']
            if plan == "Full":
                tools = Scan.objects.all()
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)

                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')

                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'Fast Speed':
                tools = Scan.objects.filter(speed='Fast')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)

                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        Task.objects.create(order_id=order.id, user=current_user, scan=scan)

                    response = HttpResponse('Done')

                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'Medium Speed':
                tools = Scan.objects.filter(speed='Medium')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')


                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'Slow Speed':
                tools = Scan.objects.filter(speed='Slow')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')


                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'Information':
                tools = Scan.objects.filter(risk='Information')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')

                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'Low Risk':
                tools = Scan.objects.filter(risk='Low')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')

                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'Medium Risk':
                tools = Scan.objects.filter(risk='Medium')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')

                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'High Risk':
                tools = Scan.objects.filter(risk='High')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')

                else:
                    response = HttpResponse('Low Credit')

            elif plan == 'Critical Risk':
                tools = Scan.objects.filter(risk='Critical')
                if tools.count() <= profile.credit:
                    profile.credit -= tools.count()
                    profile.save()
                    plan = Plan.objects.get(name=plan)
                    Order.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Order.objects.get(user=current_user, address=address, plan=plan)

                    for item in order.tools.all():
                        scan = Scan.objects.get(id=item.id)
                        txt = scan.cmd
                        cmd = txt.replace("$", order.address)
                        Task.objects.create(order_id=order.id, user=current_user, cmd=cmd)

                    response = HttpResponse('Done')


                else:
                    response = HttpResponse('Low Credit')

            else:
                response = HttpResponse('Plan Not Found')

            return response

        elif panel_type == 'custom':
            tools = request.POST.getlist('tool')
            tools = list(map(int, tools))

            if len(tools) <= profile.credit:

                if tools:
                    profile.credit -= len(tools)
                    profile.save()
                    plan = Plan.objects.get(name="Custom")
                    order = Order.objects.create(user=current_user, address=address, plan=plan)
                    order.tools.set(tools)

                    for item in tools:
                        scan = Scan.objects.get(id=item)
                        Task.objects.create(order_id=order.id, user=current_user, scan=scan)

                    response = HttpResponse('Done')

                else:
                    response = HttpResponse('List Is Empty')

            else:
                response = HttpResponse('Low Credit')

            return response

        else:
            return HttpResponse('Tab not found')

    else:
        scans = Scan.objects.all()
        plans = Plan.objects.filter(display=True)
        response = render(request, 'dashboard/scan.html', {'scans': scans, 'plans': plans})
        return response


@login_required(login_url='login')
def order(request):
    orders = Order.objects.all()
    response = render(request, 'dashboard/orders.html', {'orders': orders})
    return response


@login_required(login_url='login')
def task(request, order):
    if request.user.is_authenticated:
        current_user = request.user
        tasks = Task.objects.filter(order_id=order, user__order=current_user.id)
        order = Order.objects.get(id=order)

        information = order.found.filter(risk="Information")
        low = order.found.filter(risk="Information")
        medium = order.found.filter(risk="Medium")
        high = order.found.filter(risk="High")
        critical = order.found.filter(risk="Critical")

        total = order.found.all()

        response = render(request, 'dashboard/details.html', {
            'total': total,
            'tasks': tasks.count(),
            'count_information': information.count(),
            'count_low': low.count(),
            'count_medium': medium.count(),
            'count_high': high.count(),
            'count_critical': critical.count(),
            'count_total': total.count(),
            'information': information,
            'url': order.address,
        })

    else:
        response = render(request, 'dashboard/login.html', {})
    return response


@login_required(login_url='login')
def details(request, order):
    tasks = Task.objects.all(order_id=order)
    response = render(request, 'dashboard/details.html', {'tasks': tasks})
    return response


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            response = render(request, 'dashboard/index.html', {'user': user})
        else:
            response = HttpResponse("Username Or Password Is Wrong")
    else:
        if request.user.is_authenticated:
            user = request.user
            response = render(request, 'dashboard/index.html', {'user': user})
        else:
            response = render(request, 'dashboard/login.html', {})
    return response


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_exist = User.objects.filter(username=username)
        email_exist = User.objects.filter(email=email)
        if not user_exist and not email_exist:
            if username and email and password != '':

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                auth_login(request, user)
                response = render(request, 'dashboard/index.html', {'user': user})

            else:
                response = HttpResponse("All Field Is Required")
        else:
            response = HttpResponse("User Is Exist")
    else:
        if request.user.is_authenticated:
            response = render(request, 'dashboard/dashboard.html', {})
        else:
            response = render(request, 'dashboard/register.html', {})
    return response


def forget_password(request):
    if request.method == 'POST':
        user_data = request.POST['user_data']
        user = User.objects.filter(username=user_data)
        if not user:
            user = User.objects.filter(email=user_data)
            if not user:
                response = HttpResponse("User Not Found")
            else:
                response = HttpResponse("Done")
        else:
            response = HttpResponse("Done")
    else:
        if request.user.is_authenticated:
            response = render(request, 'dashboard/dashboard.html', {})
        else:
            response = render(request, 'dashboard/forget_password.html', {})

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
