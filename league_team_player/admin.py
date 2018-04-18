from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
# Register your models here.
from .models import *

class SwipsPlayerInfoAdmin(admin.ModelAdmin):
    list_display = ('player', 'name', 'mid_name', 'name_ko', 'mid_name_ko',\
            'name_th', 'mid_name_th', 'country', 'social', 'draft', 'school', 'ut')
    # list_editable = ['name', 'mid_name', 'name_ko', 'mid_name_ko',\
    #         'name_th', 'mid_name_th', 'country', 'social', 'draft', 'school', 'ut']

class SwipsTeamInfoAdmin(admin.ModelAdmin):
    list_display = ('team', 'name', 'mid_name', 'short_name', 'name_ko', 'mid_name_ko',\
            'name_th', 'mid_name_th', 'color', 'city', 'founded', 'last_rank',\
            'no_champions', 'manager', 'manager_ko', 'manager_th', 'social',\
            'social_ko', 'social_pt', 'social_id', 'social_th', 'social_vi', 'ut')

class SwipsLeagueInfoAdmin(admin.ModelAdmin):
    list_display = ('league', 'name')

# @admin.register(SwipsPlayerCareer)
# class SwipsPlayerCareerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'player', 'team', 'date_from', 'date_to', 'active', 'ut',
#                     'on_loan')

# @admin.register(CurryPlayer)
# class CurryPlayerAdmin(admin.ModelAdmin):
#
#     list_display = ('player', 'name', 'mid_name', 'name_ko', 'mid_name_ko', 'name_th',
#                     'mid_name_th', 'country', 'social', 'draft', 'school', 'ut', 'position')

admin.site.register(SwipsPlayerInfo,SwipsPlayerInfoAdmin)
admin.site.register(SwipsTeamInfo,SwipsTeamInfoAdmin)
admin.site.register(SwipsLeagueInfo,SwipsLeagueInfoAdmin)
