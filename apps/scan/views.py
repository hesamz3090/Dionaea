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
        if request.GET['ACTION']:
            action = request.GET['ACTION']
            scan_id = request.GET['SCAN_ID']

            if action == 'START':
                start_website_scan(scan_id)

            elif action == 'STOP':
                stop_website_scan(scan_id)

        form = WebsiteForm(request.POST)
        query = Website.objects.filter(user=request.user)

        response = render(request, 'scan/scan_website.html', {'website_list': query, 'website_form': form})

    return response