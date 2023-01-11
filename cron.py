import subprocess
import time

import standalone

standalone.run('Dionaea.settings')
from apps.scan.models import *

start_time = time.process_time()

tasks = Task.objects.filter(result='').order_by('id')[:50]

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
        task_end_time = (time.process_time() - start_time)/60
        if task.command.word in result:
            task.found = True

        task.result = result
        task.complete = True
        task.time_spend = (task_end_time - start_time)/60

        left_task = Task.objects.filter(scan=task.scan, complete=True).count()
        total_task = Task.objects.filter(scan=task.scan).count()

        if left_task == 0:
            task.scan.percent = 100
            task.scan.status = 'COMPLETED'
            scan_end_time = (time.process_time() - start_time)/60

        else:
            task.scan.percent = 100 - ((100 * left_task) / total_task)

        task.scan.save()
        task.save()

cron_end_time = (time.process_time() - start_time)/60
print(cron_end_time)

