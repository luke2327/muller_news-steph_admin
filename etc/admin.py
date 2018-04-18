from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'name', 'enetid', 'n', 'name_id',
                    'name_th', 'name_vi', 'name_pt', 'name_ko')
    list_editable = ['name', 'name_id', 'name_th', 'name_vi',
                    'name_pt', 'name_ko']
