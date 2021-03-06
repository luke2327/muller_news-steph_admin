from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'name', 'enetid', 'n', 'name_id',
                    'name_th', 'name_vi', 'name_pt', 'name_ko')
    list_editable = ['name', 'name_id', 'name_th', 'name_vi',
                    'name_pt', 'name_ko']
    list_filter = ['id', 'name', 'name_ko']
    search_fields = ('id', 'name', 'name_id', 'name_th', 'name_vi',
                    'name_pt', 'name_ko')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
