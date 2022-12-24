from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('scan_website/', scan_website, name='scan_website'),
    # path('task/<int:order>', task, name='task'),
    # path('details/<int:order>', details, name='details'),
]
