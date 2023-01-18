from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.scan.forms import *
from apps.scan.lib import *
from apps.scan.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator


@login_required(login_url='login')
def scan_website(request):
    form = WebsiteForm(request.POST)
    query = Website.objects.filter(user=request.user).order_by('id')

    if request.method == 'POST':
        if form.is_valid():
            address = create_address(form.cleaned_data.get('address'))
            if request.POST.get('submit') == 'FAST':
                message = create_website_scan(request.user.username, address, 'FAST SCAN', True)
                messages.success(request, message)
                response = HttpResponseRedirect(reverse('home'))
            else:
                description = form.cleaned_data.get('description')
                message = create_website_scan(request.user.username, address, description, False)
                messages.success(request, message)
                response = HttpResponseRedirect(reverse('scan_website'))
        else:
            message = form.errors
            messages.error(request, message)
            response = HttpResponseRedirect(reverse('scan_website'))

    else:

        page = int(request.GET.get('page')) if request.GET.get('page') else 1
        paginator = Paginator(query, 20)
        query = paginator.get_page(1)

        count_list = paginator.get_elided_page_range(number=page, on_each_side=9)
        response = render(request, 'scan/scan_website.html', {
            'website_list': query,
            'count_list': count_list,
            'website_form': form,
            'page': page,
        })

    return response


@login_required(login_url='login')
def scan_website_report(request, website_id):
    scan = Website.objects.get(id=website_id, user=request.user)
    found = Task.objects.filter(scan__id=scan.id, found=True, user=request.user)

    information_risk = found.filter(command__risk='INFORMATION')
    low_risk = found.filter(command__risk='LOW')
    medium_risk = found.filter(command__risk='MEDIUM')
    high_risk = found.filter(command__risk='HIGH')
    critical_risk = found.filter(command__risk='CRITICAL')

    if 'http://' in scan.address:
        address = scan.address.replace('http://', '')
    if 'https://' in scan.address:
        address = scan.address.replace('https://', '')
    if scan.address[-1] == '/':
        address = address[:len(address) - 1]

    found_list = []
    for item in found:
        found_row = {
            'id': item.id,
            'vulnerability_name': item.command.vulnerability.name,
            'vulnerability_description': item.command.vulnerability.description,
            'description': item.command.description,
            'tool_name': item.command.tool.name,
            'risk': item.command.risk
        }
        found_list.append(found_row)

    scan_data = {
        'id': scan.id,
        'address': address,
        'created': scan.created_on,
        'description': scan.description,
        'found': found_list,
        'information_risk_count': information_risk.count(),
        'low_risk_count': low_risk.count(),
        'medium_risk_count': medium_risk.count(),
        'high_risk_count': high_risk.count(),
        'critical_risk_count': critical_risk.count()
    }

    response = render(request, 'scan/scan_website_report.html', {
        'scan': scan_data,
    })
    return response


@login_required(login_url='login')
def scan_website_action(request, action, scan_id):
    if request.method == 'GET':

        if action == 'START':
            message = start_website_scan(scan_id)
            messages.success(request, message)

        elif action == 'STOP':
            message = stop_website_scan(scan_id)
            messages.success(request, message)

        elif action == 'DELETE':
            message = delete_website_scan(scan_id)
            messages.success(request, message)

        else:
            message = 'Action Not Found'
            messages.error(request, message)

        response = HttpResponseRedirect(reverse('scan_website'))

        return response
