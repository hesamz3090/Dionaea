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

    website = Website.objects.create(
        user=user,
        address=create_address(address),
        description=description,
        status='CREATED',
        is_fast=False
    )

    if is_fast:
        commands = commands.filter(speed='FAST')
        website.is_fast = True
        website.save()

    for command in commands:
        command_row = Command.objects.get(id=command.id)
        text = command_row.args.replace("$", address)
        text = command_row.tool.text + ' ' + text

        Task.objects.create(
            user=user,
            website=website,
            text=text,
            command=command_row
        )

    if is_fast:
        start_website_scan(website)

    message = 'Scan Added'

    return message


def ready_website_scan(id):
    website = Website.objects.get(id=id)
    website.status = 'READY'
    website.save()
    return 'Scan Is Ready'


def start_website_scan(id):
    website = Website.objects.get(id=id)
    tasks = Task.objects.filter(website=website)

    for task in tasks:
        left_task = Task.objects.filter(website=website, complete=False).count()
        total_task = Task.objects.filter(website=website).count()

        if left_task == 0:
            task.website.percent = 100
            task.website.status = 'COMPLETED'

        else:
            task.website.percent = 100 - ((100 * left_task) / total_task)
            process = subprocess.Popen(
                [task.text],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
            )

            output, err = process.communicate()
            task.result = (output + err).decode("utf-8")

            if task.command.word in task.result:
                task.found = True

        task.complete = True
        task.website.save()
        task.save()

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
