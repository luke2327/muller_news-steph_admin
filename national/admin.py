from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SwipsNationalTeamInfoWC)
class SwipsNationalTeamInfoWCAdmin(admin.ModelAdmin):
    list_display = ('team', 'name', 'fifa_ranking', 'no_champions', 'appearance',
                    'best_result', 'last_result', 'no_champions_desc',
                    'appearance_desc', 'best_result_desc', 'last_result_desc')
    list_editable = ['no_champions', 'appearance',
                    'best_result', 'last_result']
    list_filter = ['team', 'name']
    search_fields = ['team', 'name']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
@admin.register(SwipsNationalTeamInfoCompetition)
class SwipsNationalTeamInfoCompetitionAdmin(admin.ModelAdmin):
    list_display = ('team', 'competition', 'no_champions', 'appearance', 'best_result',
                    'last_result', 'no_champions_desc', 'appearance_desc', 'best_result_desc',
                    'last_result_desc', 'valid_until', 'ut')
    list_editable = ['competition', 'no_champions', 'appearance', 'best_result',
                    'last_result', 'no_champions_desc', 'appearance_desc', 'best_result_desc',
                    'last_result_desc', 'valid_until', 'ut']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    ordering = ['team']
@admin.register(SwipsNationalCompetitionInfo)
class SwipsNationalCompetitionInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_ko', 'name_pt', 'name_th',
                    'name_id', 'name_vi', 'ut',)
    list_editable = ['name', 'name_ko', 'name_pt', 'name_th',
                    'name_id', 'name_vi', 'ut']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
