from django.contrib.auth.models import User
from .models import Command, Website, Task


def create_address(address):
    if not 'http' in address:
        address = 'http://' + address
    if 'www.' in address:
        address = address.replace('www.', '')
    return address


def create_website_scan(username, address, description):
    commands = Command.objects.filter(is_available=True, tool__is_available=True)
    user = User.objects.get(username=username)
    address = create_address(address)

    scan = Website.objects.create(
        user=user,
        address=create_address(address),
        description=description,
        status='CREATED',
    )

    for command in commands:
        command_row = Command.objects.get(id=command.id)
        text = command_row.args.replace("$", address)
        text = command.tool.text + ' ' + text

        Task.objects.create(
            user=user,
            scan=scan,
            text=text,
            command=command_row
        )

    message = 'Scan Added'

    return message


def start_website_scan(id):
    website = Website.objects.get(id=id)
    website.status = 'STARTED'
    website.save()
    return 'Done'


def stop_website_scan(id):
    website = Website.objects.get(id=id)
    website.status = 'STOPPED'
    website.save()
    return 'Done'


def delete_website_scan(id):
    Task.objects.filter(scan__id=id).delete()
    Website.objects.get(id=id).delete()
    return 'Done'


def get_website_scan(id):
    website = Website.objects.get(id=id)
    return website
