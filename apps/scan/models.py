from django.db import models
from django.contrib.auth.models import User

risk_list = (
    ("INFORMATION", "INFORMATION"),
    ("LOW", "LOW"),
    ("MEDIUM", "MEDIUM"),
    ("HIGH", "HIGH"),
    ("CRITICAL", "CRITICAL")
)

time_list = (
    ("FAST", "FAST"),
    ("MEDIUM", "MEDIUM"),
    ("SLOW", "SLOW"),
)

status_list = (
    ("CREATED", "CREATED"),
    ("READY", "READY"),
    ("STARTED", "STARTED"),
    ("STOPPED", "STOPPED"),
    ("COMPLETED", "COMPLETED"),
)


class Tool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=11)
    text = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Vulnerability(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Command(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    args = models.TextField()
    risk = models.CharField(choices=risk_list, max_length=11)
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    alert = models.TextField(max_length=100)
    speed = models.CharField(choices=time_list, max_length=6)
    word = models.CharField(max_length=100)
    spend_time = models.IntegerField(blank=True, null=True, editable=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.args


class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    percent = models.IntegerField(default=0)
    status = models.CharField(choices=status_list, max_length=9, default='CREATED')
    is_fast = models.BooleanField(default=True)

    def __str__(self):
        return self.address

    def save_model(self, request, obj):
        # self.address = create_address(self.address)
        self.user = request.user
        obj.save()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    found = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    result = models.TextField(blank=True)
