import time
import psutil
import requests
from multiprocessing import Process
import standalone

standalone.run('Dionaea.settings')
from website.models import *
from apps.scan.lib import *

print('Started')
setting = Setting.objects.first()

if not setting.cron:
    setting.cron = True
    setting.save()

    websites = Website.objects.filter(status='STARTED').order_by('id')
    print(websites.count())
    i = 1
    for website in websites:
        CPU = psutil.cpu_percent(9)
        print(website.id, CPU, i)
        # RAM = psutil.virtual_memory()[3] / 1073741824
        if CPU <= setting.max_cpu_percent:
            p = Process(target=start_website_scan, args=(website.id,))
            p.start()
            p.join()
            i += 1
        else:
            break

    setting.cron = False
    setting.save()

print('Ended')

# url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=Start'
# requests.get(url)

# path_list = ['/home/gardener/', '/home/gardener/Dionaea/']
# setting = Setting.objects.get(user__username='hesamz3090')
# start_time = time.time()

# Website.objects.filter(status='COMPLETED', is_fast=True).delete()
# website_obj = Website.objects.filter(status='STARTED')
# website = Website.objects.get(id=806)
#
# tasks = Task.objects.filter(scan=website)

# fast_task = tasks.filter(command__speed='FAST')
# medium_task = tasks.filter(command__speed='MEDIUM')
# slow_task = tasks.filter(command__speed='SLOW')
# start_time = time.time()
# for task in tasks:
#     start_task_time = time.time()
#     process = subprocess.Popen(
#         [task.text],
#         stdin=subprocess.PIPE,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         shell=True
#     )
#
#     output, err = process.communicate()
#     result = (output + err).decode("utf-8")
#
#     if task.command.word in result:
#         task.found = True
#
#     task.result = result
#     task.complete = True
#     task.command.spend_time = abs(int((time.time() - start_task_time)))
#     task.save()
#     task.command.save()

# url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=({task.command.id})/ {task.command.spend_time} S'
# requests.get(url)

# end_time = abs(int((time.time() - start_time)))
# url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=END {end_time} S'
# requests.get(url)

# for task in tasks:
#     print(task.)
# for obj in website_obj:
#     task_count = Task.objects.filter(scan=obj).count()
#     if task_count == 0:
#         obj.status = 'COMPLETED'
#         obj.percent = 100
#         obj.save()

# if not setting.is_active:
#     url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=Not Active'
#     requests.get(url)
#     setting.is_active = True
#     setting.save()
#
#     tasks = Task.objects.filter(
#         complete=False,
#         scan__status='STARTED',
#         scan__is_fast=False
#     ).order_by('id')[:setting.max_task]

# for task in tasks:
#     process = subprocess.Popen(
#         [task.text],
#         stdin=subprocess.PIPE,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         shell=True
#     )
#
#     output, err = process.communicate()
#     result = (output + err).decode("utf-8")
#
#     if task.command.word in result:
#         task.found = True
#
#     task.result = result
#     task.complete = True
#     task.time_spend = abs(round((time.time() - start_time) / 60, 2)) - task.time_spend if task.time_spend else abs(round((time.time() - start_time) / 60, 2))
#
#     left_task = Task.objects.filter(scan=task.scan, complete=False).count()
#     total_task = Task.objects.filter(scan=task.scan).count()
#
#     if left_task == 0:
#         task.scan.percent = 100
#         task.scan.status = 'COMPLETED'
#
#     else:
#         task.scan.percent = 100 - ((100 * left_task) / total_task)
#
#     task.scan.save()
#     task.save()

#     cron_end_time = abs(round((time.time() - start_time) / 60, 2))
#     if cron_end_time > setting.spend_time:
#         setting.spend_time = cron_end_time
#         setting.save()
#
#     for path in path_list:
#         for file in os.listdir(path):
#             if os.path.isfile(os.path.join(path, file)) and 'temp' in file:
#                 os.remove(path + file)
#
#     url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text={cron_end_time}'
#     requests.get(url)
#
#     setting.is_active = True
#     setting.save()
#
# else:
#     url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=Activated'
#     requests.get(url)
#
# url = f'https://api.telegram.org/bot5358693137:AAG7SgFfuo2VtjWc3nR_r8RhpXfNSAXALKI/sendMessage?chat_id=5970578512&text=END'
# requests.get(url)
