from django.contrib import admin
from .models import *


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'is_available')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', 'tool', 'risk', 'speed', 'vulnerability', 'is_available')
    list_filter = ('tool', 'risk', 'speed', 'vulnerability', 'is_available')
    search_fields = ('description', 'arg', 'alert')

    def is_available(self, obj):
        if not obj.tool.is_available:
            obj.is_available = False
        else:
            obj.is_available = True
        obj.save()


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'created_on', 'percent', 'filter')
    list_filter = ('user', 'created_on', 'percent', 'filter')
    search_fields = ('user', 'address')

    def get_queryset(self, request):
        qs = super(WebsiteAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'scan', 'text', 'found')
    list_filter = ('found', 'user')
    search_fields = ('scan', 'user', 'id')
