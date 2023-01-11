import subprocess
import time

import standalone

standalone.run('Dionaea.settings')
from apps.scan.models import *

start_time = time.time()

tasks = Task.objects.filter(complete=False).order_by('id')[:50]

for task in tasks:
    if task.scan.status == 'STOPPED':
        task.delete()
    elif task.scan.status == 'STARTED':
        process = subprocess.Popen(
            [task.text],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        output, err = process.communicate()
        result = (output + err).decode("utf-8")
        task_end_time = (time.time() - start_time) / 60
        if task.command.word in result:
            task.found = True

        task.result = result
        task.complete = True
        task.time_spend = abs(round((task_end_time - start_time) / 60, 2))

        left_task = Task.objects.filter(scan=task.scan, complete=False).count()
        total_task = Task.objects.filter(scan=task.scan).count()

        if left_task == 0:
            task.scan.percent = 100
            task.scan.status = 'COMPLETED'
            scan_end_time = abs(round((time.time() - start_time) / 60, 2))

        else:
            task.scan.percent = 100 - ((100 * left_task) / total_task)

        task.scan.save()
        task.save()

if tasks.count() == 0:
    websites = Website.objects.filter(complete=False)
    for website in websites:
        website.status = 'COMPLETED'
        website.percent = 100
        website.save()


cron_end_time = abs(round((time.time() - start_time) / 60, 2))
print(cron_end_time)
