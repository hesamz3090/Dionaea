import subprocess
import time
import os
import standalone

standalone.run('Dionaea.settings')
from apps.scan.models import *
from website.models import *

url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=END'

path_list = ['/home/gardener/', '/home/gardener/Dionaea/']
setting = Setting.objects.get(user__username='hesamz3090')
start_time = time.time()

website_obj = Website.objects.filter(status='STARTED')

for obj in website_obj:
    task_count = Task.objects.filter(scan=obj).count()
    if task_count == 0:
        obj.status = 'COMPLETED'
        obj.percent = 100
        obj.save()

if not setting.is_active:
    setting.is_active = True
    setting.save()

    tasks = Task.objects.filter(complete=False, scan__status='STARTED').order_by('id')[:setting.max_task]
    for task in tasks:
        process = subprocess.Popen(
            [task.text],
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
        task.time_spend = abs(round((time.time() - start_time) / 60, 2)) - task.time_spend

        left_task = Task.objects.filter(scan=task.scan, complete=False).count()
        total_task = Task.objects.filter(scan=task.scan).count()

        if left_task == 0:
            task.scan.percent = 100
            task.scan.status = 'COMPLETED'

        else:
            task.scan.percent = 100 - ((100 * left_task) / total_task)

        task.scan.save()
        task.save()

    cron_end_time = abs(round((time.time() - start_time) / 60, 2))
    if cron_end_time > setting.spend_time:
        setting.spend_time = cron_end_time
        setting.save()

    for path in path_list:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)) and 'temp' in file:
                os.remove(path + file)

    url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=END'

    setting.is_active = False
    setting.save()
