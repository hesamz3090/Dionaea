from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('debugger/', debugger, name='debugger'),
    path('rules/', rules, name='rules'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]