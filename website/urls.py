from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('ticket/', ticket, name='ticket'),
    path('profile/', profile, name='profile'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forget/', forget, name='forget'),
    path('logout/', logout, name='logout'),
]