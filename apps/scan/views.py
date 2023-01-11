from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.scan.forms import *
from apps.scan.lib import *
from apps.scan.models import *


@login_required(login_url='login')
def scan_website(request):
    form = WebsiteForm(request.POST)
    query = Website.objects.filter(user=request.user)

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data.get('address'))
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
            form = WebsiteForm(request.POST)
            query = Website.objects.filter(user=request.user)
            response = render(request, 'scan/scan_website.html', {
                'website_list': query,
                'website_form': form,
                'message': message,
                'type': 'ERORR',
            })

    else:
        response = render(request, 'scan/scan_website.html', {
            'website_list': query,
            'website_form': form,
        })

    return response


@login_required(login_url='login')
def scan_website_report(request, website_id):
    scan = Website.objects.get(id=website_id, user=request.user)
    found = Task.objects.filter(scan__id=scan.id, found=True, user=request.user)
    address = scan.address.replace('http://', '') or scan.address.replace('https://', '')
    information_risk = found.filter(command__risk='Information')
    low_risk = found.filter(command__risk='Low')
    medium_risk = found.filter(command__risk='Medium')
    high_risk = found.filter(command__risk='High')
    critical_risk = found.filter(command__risk='Critical')

    found_list = []
    for item in found:
        found_row = {
            'id': item.id,
            'vulnerability_name': item.command.vulnerability.name,
            'description': item.command.description,
            'tool_name': item.command.tool.name,
            'risk': item.command.risk
        }
        found_list.append(found_row)

    scan_data = {
        'id': scan.id,
        'address': address,
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
        form = WebsiteForm(request.POST)
        query = Website.objects.filter(user=request.user)

        if action == 'START':
            message = start_website_scan(scan_id)

        elif action == 'STOP':
            message = stop_website_scan(scan_id)

        elif action == 'DELETE':
            message = delete_website_scan(scan_id)

        response = render(request, 'scan/scan_website.html', {
            'website_list': query,
            'website_form': form,
            'message': message,
            'type': 'MESSAGE',
        })

        return response
