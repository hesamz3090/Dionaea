from django.contrib.auth.models import User
from .models import Command, Website, Task
import subprocess


def create_address(address):
    if not 'http' in address:
        address = 'http://' + address
    if 'www.' in address:
        address = address.replace('www.', '')
    return address


def create_website_scan(username, address, description, is_fast):
    commands = Command.objects.filter(is_available=True, tool__is_available=True)
    user = User.objects.get(username=username)
    address = create_address(address)

    scan = Website.objects.create(
        user=user,
        address=create_address(address),
        description=description,
        status='CREATED',
        is_fast=False
    )

    if is_fast:
        commands = commands.filter(speed='FAST')
        scan.is_fast = True
        scan.save()

    for command in commands:
        command_row = Command.objects.get(id=command.id)
        text = command_row.args.replace("$", address)
        text = command_row.tool.text + ' ' + text

        task = Task.objects.create(
            user=user,
            scan=scan,
            text=text,
            command=command_row
        )

        if is_fast:
            process = subprocess.Popen(
                [text],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
            )

            output, err = process.communicate()
            result = (output + err).decode("utf-8")

            if task.command.word in result:
                task.found = True

            task.result = result
            task.complete = True

    message = 'Scan Added'

    return message


def start_website_scan(id):
    website = Website.objects.get(id=id)
    website.status = 'STARTED'
    website.save()
    return 'Scan Started'


def stop_website_scan(id):
    website = Website.objects.get(id=id)
    website.status = 'STOPPED'
    website.save()
    return 'Scan Stopped'


def delete_website_scan(id):
    Task.objects.filter(scan__id=id).delete()
    Website.objects.get(id=id).delete()
    return 'Scan Deleted'


def get_website_scan(id):
    website = Website.objects.get(id=id)
    return website
