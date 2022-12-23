from django.shortcuts import render
from .models import *


def index(request):
    response = render(request, 'home/index.html', {})
    return response


def debugger(request):
    response = render(request, 'home/debugger.html', {})
    return response


def rules(request):
    response = render(request, 'home/rules.html', {})
    return response


def about(request):
    response = render(request, 'home/about.html', {})
    return response


def contact(request):
    response = render(request, 'home/contact.html', {})
    return response


def page_not_found(request, exception):
    response = render(request, 'home/404.html', {})
    return response


def server_error(request):
    response = render(request, 'home/500.html', {})
    return response


def permission_denied(request, exception):
    response = render(request, 'home/403.html', {})
    return response


def bad_request(request, exception):
    response = render(request, 'home/400.html', {})
    return response
