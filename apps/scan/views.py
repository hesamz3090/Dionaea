from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.scan.forms import *
from apps.scan.lib import *
from apps.scan.models import *


@login_required(login_url='login')
def scan_website(request):
    form = WebsiteForm(request.POST)
    query = Website.objects.filter(user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            address = create_address(form.cleaned_data.get('address'))
            description = form.cleaned_data.get('description')
            message = create_website_scan(request.user.username, address, description)
            response = render(request, 'scan/scan_website.html', {
                'website_list': query,
                'website_form': form,
                'message': message,
                'type': 'MESSAGE',
            })
        else:
            message = form.errors
            response = render(request, 'scan/scan_website.html', {
                'website_list': query,
                'website_form': form,
                'message': message,
                'type': 'ERORR',
            })

    else:
        response = render(request, 'scan/scan_website.html', {'website_list': query, 'website_form': form})

    return response

#
# @login_required(login_url='login')
# def order(request):
#     orders = Website.objects.all()
#     response = render(request, 'dashboard/orders.html', {'orders': orders})
#     return response
#
#
# @login_required(login_url='login')
# def task(request, order):
#     if request.user.is_authenticated:
#         current_user = request.user
#         tasks = Task.objects.filter(order_id=order, user__order=current_user.id)
#         order = Website.objects.get(id=order)
#
#         information = order.found.filter(risk="Information")
#         low = order.found.filter(risk="Information")
#         medium = order.found.filter(risk="Medium")
#         high = order.found.filter(risk="High")
#         critical = order.found.filter(risk="Critical")
#
#         total = order.found.all()
#
#         response = render(request, 'dashboard/details.html', {
#             'total': total,
#             'tasks': tasks.count(),
#             'count_information': information.count(),
#             'count_low': low.count(),
#             'count_medium': medium.count(),
#             'count_high': high.count(),
#             'count_critical': critical.count(),
#             'count_total': total.count(),
#             'information': information,
#             'url': order.address,
#         })
#
#     else:
#         response = render(request, 'dashboard/login.html', {})
#     return response
#
#
# @login_required(login_url='login')
# def details(request, order):
#     tasks = Task.objects.all(order_id=order)
#     response = render(request, 'dashboard/details.html', {'tasks': tasks})
#     return response
