from django.http import HttpResponse
from django.shortcuts import render


def api(request):
    response = HttpResponse('Test')
    return response


def docs(request):
    response = render(request, 'docs.html', {})
    return response
