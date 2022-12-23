from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from apps.dashboard.models import Profile
from apps.scan.models import *


@login_required(login_url='login')
def scan_website(request):
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
                    Scan.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)

                    order = Scan.objects.get(user=current_user, address=address, plan=plan)

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
                    Scan.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)

                    order = Scan.objects.get(user=current_user, address=address, plan=plan)

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
                    Scan.objects.create(user=current_user, address=address, plan=plan).tools.set(tools)
                    order = Scan.objects.get(user=current_user, address=address, plan=plan)

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
    orders = Scan.objects.all()
    response = render(request, 'dashboard/orders.html', {'orders': orders})
    return response


@login_required(login_url='login')
def task(request, order):
    if request.user.is_authenticated:
        current_user = request.user
        tasks = Task.objects.filter(order_id=order, user__order=current_user.id)
        order = Scan.objects.get(id=order)

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
