from django.urls import path
from .views import *

urlpatterns = [
    path('scan_website/', scan_website, name='scan_website'),
    path('scan_website_action/<str:action>/<int:scan_id>', scan_website_action, name='scan_website_action'),
    path('scan_website_report/<int:website_id>', scan_website_report, name='scan_website_report'),
]
