from django.shortcuts import render
from django.http import HttpResponse
from apps.scan.models import *


def index(request):
    scans = Scan.objects.all()
    plans = Plan.objects.filter(display=True)
    response = render(request, 'home/debugger.html', {'scans': scans, 'plans': plans})
    return response


def test(request):
    return HttpResponse("Test")
