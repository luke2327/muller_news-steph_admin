from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CurryInfoDbModify)
class CurryInfoDbModifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'migrate_item', 'type',
                    'desc', 'ut', 'valid_until')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
@admin.register(CurryInfoImageModify)
class CurryInfoImageModifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'type', 'desc', 'ut', 'valid_until')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
