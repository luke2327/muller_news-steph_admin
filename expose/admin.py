from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CurryExposePostLog)
class CurryExposePostLog(admin.ModelAdmin):
    list_display = ('id', 'desc', 'user', 'ut', 'target')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
@admin.register(CurryExposeTarget)
class CurryExposeTargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'ut')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
