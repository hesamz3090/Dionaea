from .forms import *
from django.shortcuts import render


def index(request):
    response = render(request, 'home/index.html', {})
    return response


def rules(request):
    response = render(request, 'home/rules.html', {})
    return response


def about(request):
    response = render(request, 'home/about.html', {})
    return response


def contact(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ContactForm()
        response = render(request, 'home/contact.html', context)

    elif request.method == 'POST':
        back_url = request.META.get('HTTP_REFERER')
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            message = 'Done'
            response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})

        else:
            message = form.errors
            response = render(request, 'home/message.html', {'message': message, 'back_url': back_url})

    else:
        response = render(request, 'home/errors/404.html', {})
    return response


def page_not_found(request, exception):
    response = render(request, 'home/errors/404.html', {})
    return response


def server_error(request):
    response = render(request, 'home/errors/500.html', {})
    return response


def permission_denied(request, exception):
    response = render(request, 'home/errors/403.html', {})
    return response


def bad_request(request, exception):
    response = render(request, 'home/errors/400.html', {})
    return response
