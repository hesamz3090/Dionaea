from django.contrib.auth.models import User
from django.db import models

subject_list = (
    ("message", "message"),
    ("bug", "bug"),
    ("idea", "idea"),
    ("criticism", "criticism"),
    ("questions", "questions"),
    ("other", "other"),
)

status_list = (
    ("Opened", "Opened"),
    ("Working", "Working"),
    ("Answered", "Answered"),
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    left_day = models.IntegerField(default=0)
    free_try = models.BooleanField(default=False)
    user_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Setting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Document(models.Model):
    name = models.CharField(max_length=15)
    image = models.FileField(upload_to='document/')
    descriptions = models.CharField(max_length=50, blank=True, null=True)
    url = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, editable=False, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(choices=subject_list, max_length=9)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(choices=subject_list, max_length=9)
    status = models.CharField(choices=status_list, max_length=8, default='Opened')
    message = models.TextField(default='-')
    answer = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Payment(models.Model):
    title = models.CharField(max_length=200)
    code = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    result = models.CharField(max_length=30, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
