from django.urls import path
from .views import *

urlpatterns = [
    path('', api, name='api'),
    path('docs/', docs, name='docs'),
]