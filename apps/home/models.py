from django.db import models
from django.contrib.auth.models import User

type_list = (
    ("ticket", "ticket"),
    ("contact", "contact"),
)

subject_list = (
    ("message", "message"),
    ("bug", "bug"),
    ("idea", "idea"),
    ("criticism", "criticism"),
    ("questions", "questions"),
    ("other", "other"),
)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(choices=type_list, max_length=200)
    subject = models.CharField(choices=subject_list, max_length=200)
    message = models.TextField()
    answer = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
