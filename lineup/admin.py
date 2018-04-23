from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
# Register your models here.
from .models import *

class SwipsLineupCustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'team', 'lineup_number', 'shirt_number', 'position', 'name', 'ut')
    list_editable = ['match_id', 'team', 'lineup_number', 'shirt_number', 'position', 'name', 'ut']
    change_list_template = 'admin/steph_admin/change_list_lineup.html'
    def has_add_permission(self, request):
        return False

class SwipsMatchDetailCustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'team_id', 'lineup_number', 'shirt_number', 'name', 'type', 'minute', 'ut')
    list_editable = ['match_id', 'team_id', 'lineup_number', 'shirt_number', 'name', 'type', 'minute', 'ut']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
admin.site.register(SwipsLineupCustom,SwipsLineupCustomAdmin)
admin.site.register(SwipsMatchDetailCustom,SwipsMatchDetailCustomAdmin)
