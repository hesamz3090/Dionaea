from django.db import models
from django.contrib.auth.models import User
# from .lib import create_address

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
    text = models.TextField()
    risk = models.CharField(choices=risk_list, max_length=11)
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    alert = models.TextField(max_length=100)
    speed = models.CharField(choices=time_list, max_length=6)
    word = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.text


class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    percent = models.IntegerField(default=0)
    filter = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(choices=status_list, max_length=9, default='new')

    def __str__(self):
        return f'{self.user} , {self.address}'

    def save_model(self, request, obj):
        # self.address = create_address(self.address)
        self.user = request.user
        obj.save()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scan = models.ForeignKey(Website, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    found = models.BooleanField(default=False)
    result = models.TextField(blank=True)
