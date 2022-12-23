from django.contrib import admin
from .models import *


@admin.register(Tool)
class Tool(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Scan)
class Scan(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'created_on', 'percent', 'filter')
    list_filter = ('user', 'created_on', 'percent', 'filter')
    search_fields = ('user', 'address')

    def get_queryset(self, request):
        qs = super(Scan, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'user', 'scan', 'text', 'found')
    list_filter = ('found', 'user')
    search_fields = ('scan', 'user', 'id')


@admin.register(Vulnerability)
class Vulnerability(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Command)
class Command(admin.ModelAdmin):
    pass
