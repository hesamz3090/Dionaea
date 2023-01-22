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
    process_list = []
    for website in websites:
        CPU = psutil.cpu_percent(9)
        print(website.id, CPU, i)
        # RAM = psutil.virtual_memory()[3] / 1073741824
        if CPU <= setting.max_cpu_percent:
            p = Process(target=start_website_scan, args=(website.id,))
            p.start()
            process_list.append(p)
            i += 1
        else:
            break

    i = 1
    for process in process_list:
        process.join()
        print(i, 'join')
        i += 1

    setting.cron = False
    setting.save()

print('Ended')
