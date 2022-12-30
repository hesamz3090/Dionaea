import subprocess
import standalone

standalone.run('Dionaea.settings')
from apps.scan.models import *

tasks = Task.objects.filter(result='').order_by('id')[:50]

for task in tasks:
    if task.scan.status == 'Closed':
        task.delete()
    else:
        process = subprocess.Popen(
            [task.text],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        output, err = process.communicate()
        result = output + err

        if task.scan.word in str(result):
            task.found = True

        task.result = result

        left_task = Task.objects.filter(scan=task.scan, result='').count()
        total_task = Task.objects.filter(scan=task.scan).count()
        task.scan.percent = ((100 * left_task) / total_task)

        task.save()

