from django.contrib import admin
from .models import *


@admin.register(Scan)
class Scan(admin.ModelAdmin):
    list_display = ('id', 'name', 'risk', 'speed')
    list_filter = ('risk', 'speed')
    search_fields = ('name', 'description', 'cmd', 'error', 'fix')


@admin.register(Tool)
class Tool(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Plan)
class Plan(admin.ModelAdmin):
    list_display = ('id', 'name', 'display')
    list_filter = ('name', 'display')
    search_fields = ('name',)


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'created_on', 'percent', 'plan')
    list_filter = ('user', 'created_on', 'percent', 'plan')
    search_fields = ('user', 'address')

    def get_queryset(self, request):
        qs = super(Order, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'order', 'user')
    list_filter = ('order', 'user')
    search_fields = ('order', 'user')


@admin.register(Bug)
class Bug(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)