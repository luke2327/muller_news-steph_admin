from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(CurryAdBalance)
class CurryAdBalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'weight', 'country_cd', 'os', 'valid_until',
                    'ut', 'advertiser', 'link', 'image_link', 'ad_type',
                    'client_version', 'include_lower_versions',
                    'include_upper_versions')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    search_fields = ('id', 'type', 'weight', 'country_cd', 'os', 'valid_until',
                    'ut', 'advertiser', 'link', 'image_link', 'ad_type')

    ordering = ['-id']

@admin.register(CurryRdsScaleModifier)
class CurryRdsScaleModifierAdmin(admin.ModelAdmin):
    list_display = ('id','time','number','description','status','ut','user')
    change_list_template = 'admin/steph_admin/change_list_custom.html'

@admin.register(SwipsPush)
class SwipsPushAdmin(admin.ModelAdmin):
    list_display = ('id','push_type','table_name','row_id','status',
                    'delayed_until','ref1','ref2','ref3','ref4','ref5',
                    'refstr1','refstr2','refstr3','ut')
    search_fields = ['push_type', 'table_name', 'row_id', 'status',
                      'ref1', 'ref2', 'ref3', 'ref4', 'ref5', 'refstr1',
                      'refstr2', 'refstr3']
    list_filter = ['push_type', 'table_name', 'row_id', 'status', 'ref1', 'ref2', 'ref3', 'ref4', 'ref5', 'refstr1', 'refstr2']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
