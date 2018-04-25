from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
from django.utils.html import format_html
# Register your models here.
from .models import *

class SwipsPlayerInfoAdmin(admin.ModelAdmin):
    list_display = ('player', 'name', 'mid_name', 'name_ko', 'mid_name_ko',\
            'name_th', 'mid_name_th', 'country', 'social', 'draft', 'school', 'ut')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
    list_filter = ['player', 'name', 'name_ko', 'name_th',
                      'mid_name_ko', 'mid_name_th']
    search_fields = ['player', 'name', 'name_ko', 'name_th',
                              'mid_name_ko', 'mid_name_th']
    # list_editable = ['name', 'mid_name', 'name_ko', 'mid_name_ko',\
    #         'name_th', 'mid_name_th', 'country', 'social', 'draft', 'school', 'ut']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
class SwipsTeamInfoAdmin(admin.ModelAdmin):
    list_display = ('team', 'name', 'mid_name', 'short_name', 'name_ko', 'mid_name_ko',\
            'name_th', 'mid_name_th', 'color', 'city', 'founded', 'last_rank',\
            'no_champions', 'manager', 'manager_ko', 'manager_th', 'social',\
            'social_ko', 'social_pt', 'social_id', 'social_th', 'social_vi', 'ut')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
    list_filter = ['team', 'name', 'name_ko', 'name_th',
                      'mid_name_ko', 'mid_name_th']
    search_fields = ['team', 'name', 'name_ko', 'name_th',
                              'mid_name_ko', 'mid_name_th']
class SwipsLeagueInfoAdmin(admin.ModelAdmin):
    list_display = ('league', 'name', 'mid_name', 'short_name', 'name_ko',
                    'name_pt', 'name_th', 'name_id', 'name_vi', 'no_teams',
                    'founded', 'last_champion', 'social_link', 'social_link_ko',
                    'social_link_id', 'social_link_th', 'social_link_vi',
                    'social_link_en', 'color', 'category', 'host', 'ut')
    list_filter = ['league', 'name', 'name_ko', 'name_th',
                      'name_pt', 'name_id', 'name_vi', 'mid_name']
    search_fields = ['league', 'name', 'name_ko', 'name_th',
                              'name_pt', 'name_id', 'name_vi', 'mid_name']
    list_display_links = ['league', ]
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
    def social_linker(self, object):
        return format_html("<div style='width:200px; word-break:break-word;'>\
                            <a href='{}'>{}</a></div>",object,object)
    def social_link(self, obj):
        if obj.social is None:
            return None
        else:
            return self.social_linker(obj.social)
    def social_link_ko(self, obj):
        if obj.social_ko is None:
            return None
        else:
            return self.social_linker(obj.social_ko)
    def social_link_id(self, obj):
        if obj.social_id is None:
            return None
        else:
            return self.social_linker(obj.social_id)
    def social_link_th(self, obj):
        if obj.social_th is None:
            return None
        else:
            return self.social_linker(obj.social_th)
    def social_link_vi(self, obj):
        if obj.social_vi is None:
            return None
        else:
            return self.social_linker(obj.social_vi)
    def social_link_en(self, obj):
        if obj.social_en is None:
            return None
        else:
            return self.social_linker(obj.social_en)

@admin.register(SwipsPlayerCareer)
class SwipsPlayerCareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'team', 'date_from_', 'date_to_', 'active', 'ut',
                    'on_loan')
    def date_from_(self, obj):
        if '0000-00-00' in str(obj.date_from):
            return None
        else:
            return obj.date_from
    def date_to_(self, obj):
        if '0000-00-00' in str(obj.date_to):
            return None
        else:
            return obj.date_to

@admin.register(CurryPlayer)
class CurryPlayerAdmin(admin.ModelAdmin):

    list_display = ('player', 'name', 'mid_name', 'name_ko', 'mid_name_ko', 'name_th',
                    'mid_name_th', 'country', 'social', 'draft', 'school', 'ut', 'position')

admin.site.register(SwipsPlayerInfo,SwipsPlayerInfoAdmin)
admin.site.register(SwipsTeamInfo,SwipsTeamInfoAdmin)
admin.site.register(SwipsLeagueInfo,SwipsLeagueInfoAdmin)
