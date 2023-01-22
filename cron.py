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


websites_started = Website.objects.filter(status='STARTED').order_by('id')
websites_working = Website.objects.filter(status='WORKING').order_by('id')

websites = websites_started if websites_working.count() else websites_working

process_list = []
for website in websites:
    CPU = psutil.cpu_percent(9)

    # RAM = psutil.virtual_memory()[3] / 1073741824
    if CPU <= setting.max_cpu_percent:
        website.status = 'WORKING'
        p = Process(target=start_website_scan, args=(website.id,))
        p.start()
        process_list.append(p)
        website.save()

    else:
        break

for process in process_list:
    process.join()


print('Ended')
