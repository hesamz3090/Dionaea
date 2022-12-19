from django.db import models
from django.contrib.auth.models import User

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


class Tool(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Bug(models.Model):
    name = models.CharField(max_length=100, blank=True)
    tips = models.TextField(max_length=500)
    fix = models.TextField(max_length=500)

    def __str__(self):
        return str(self.id)


class Scan(models.Model):
    name = models.CharField(max_length=100)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    cmd = models.CharField(max_length=100)
    risk = models.CharField(choices=risk_list, max_length=11)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    error = models.TextField(max_length=500)
    speed = models.CharField(choices=time_list, max_length=6)
    word = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    tools = models.ManyToManyField(Scan, related_name='tools')
    found = models.ManyToManyField(Scan, blank=True, related_name='bugs')
    created_on = models.DateTimeField(auto_now_add=True)
    percent = models.IntegerField(default=0)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.address)


class Task(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scan = models.ForeignKey(Scan, on_delete=models.SET_NULL, null=True)
    result = models.TextField(max_length=500, blank=True)

