from django.db import models
from django.contrib.auth.models import User
import re
from urllib.parse import urlsplit

risk_list = (
    ("Information", "Information"),
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
    ("Critical", "Critical")
)

time_list = (
    ("Fast", "Fast"),
    ("Medium", "Medium"),
    ("Slow", "Slow"),
)

status_list = (
    ("new", "New"),
    ("working", "Working"),
    ("completed", "Completed"),
)


class Tool(models.Model):
    name = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Vulnerability(models.Model):
    name = models.CharField(max_length=50)
    tips = models.TextField()
    fix = models.TextField()

    def __str__(self):
        return self.name


class Command(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    text = models.CharField(choices=risk_list, max_length=100)
    risk = models.CharField(choices=risk_list, max_length=11)
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    alert = models.TextField(max_length=100)
    speed = models.CharField(choices=time_list, max_length=6)
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Scan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    percent = models.IntegerField(default=0)
    filter = models.CharField(max_length=50)
    status = models.CharField(choices=status_list, max_length=9)

    def url_maker(url):
        if not re.match(r'http(s?)\:', url):
            url = 'http://' + url
        parsed = urlsplit(url)
        host = parsed.netloc
        if host.startswith('www.'):
            host = host[4:]
        return host

    def __str__(self):
        return f'{self.user} , {self.address}'

    def save(self, *args, **kwargs):
        self.address = self.url_maker(self.address)
        super(Scan, self).save(*args, **kwargs)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scan = models.ForeignKey(Scan, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    found = models.BooleanField(default=False)
    result = models.TextField(blank=True)
