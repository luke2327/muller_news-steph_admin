from django.contrib import admin
from .models import *
from django.utils.html import format_html
from steph.util.util import Util
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'name', 'tournament_stagefk', 'startdate',
                    'eventstatusfk', 'status_type', 'status_descfk', 'enetid',
                    'enetsportid', 'n', 'ut', 'locked')
    list_display_links = ['id',]
    list_filter = ['tournament_stagefk', 'status_type', 'status_descfk']
    search_fields = ['id', 'name', 'startdate',
                              'status_type', 'status_descfk']
    ordering = ['-startdate']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
         return True

    def has_delete_permission(self, request, obj=None):
         return False
@admin.register(CurryFixturesInfo)
class CurryFixturesInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startdate', 'league', 'league_name',
                    'broadcast_id_', 'broadcast_th_', 'broadcast_vn_',
                    'broadcast_br_', 'broadcast_kr_', 'broadcast_ph_')
    search_fields = ['name', 'league_name']
    list_filter = ['name', 'league', 'league_name', 'startdate']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return False

    def broadcast_id_(self, obj):
        return Util().get_popover('admin', 'swips_fixtures_info', 'id', obj.id,\
                           'broadcast_id', obj.broadcast_id, 'text')
    def broadcast_th_(self, obj):
        return Util().get_popover('admin', 'swips_fixtures_info', 'id', obj.id,\
                           'broadcast_th', obj.broadcast_th, 'text')
    def broadcast_vn_(self, obj):
        return Util().get_popover('admin', 'swips_fixtures_info', 'id', obj.id,\
                           'broadcast_vn', obj.broadcast_vn, 'text')
    def broadcast_br_(self, obj):
        return Util().get_popover('admin', 'swips_fixtures_info', 'id', obj.id,\
                           'broadcast_br', obj.broadcast_br, 'text')
    def broadcast_kr_(self, obj):
        return Util().get_popover('admin', 'swips_fixtures_info', 'id', obj.id,\
                           'broadcast_kr', obj.broadcast_kr, 'text')
    def broadcast_ph_(self, obj):
        return Util().get_popover('admin', 'swips_fixtures_info', 'id', obj.id,\
                           'broadcast_ph', obj.broadcast_ph, 'text')

@admin.register(CurryMajorFixtures)
class CurryMajorFixturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'league', 'home_team', 'away_team',
                    'status_type', 'day', 'utc', 'kst')
    search_fields = ['id','league', 'home_team', 'away_team']
    list_filter = ['league',]
    list_filter = ['league', 'utc']
    change_list_template = 'admin/steph_admin/change_list_custom.html'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
         return True

    def has_delete_permission(self, request, obj=None):
         return False
@admin.register(SwipsFixturesInfo)
class SwipsFixturesInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'broadcast_id', 'broadcast_th', 'broadcast_vn',
                    'broadcast_br', 'broadcast_kr', 'broadcast_ph', 'ut')
    search_fields = ['id', 'ut']
    list_filter = ['ut',]
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
         return True

    def has_delete_permission(self, request, obj=None):
         return False
