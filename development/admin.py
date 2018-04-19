from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CurryAdBalance)
class CurryAdBalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'weight', 'country_cd', 'os', 'valid_until',
                    'ut', 'advertiser', 'link', 'image_link', 'ad_type')
