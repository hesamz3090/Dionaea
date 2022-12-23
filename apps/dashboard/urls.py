from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='dashboard'),
    path('scan/', scan, name='scan'),
    path('order/', order, name='order'),
    path('task/<int:order>', task, name='task'),
    path('details/<int:order>', details, name='details'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forget_password/', forget_password, name='forget_password'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
