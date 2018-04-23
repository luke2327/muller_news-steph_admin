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
    list_filter = ['status_type',]
    search_fields = ['name', 'id',]
    change_list_template = 'admin/steph_admin/change_list_custom.html'
@admin.register(CurryFixturesInfo)
class CurryFixturesInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startdate', 'league', 'league_name',
                    'broadcast_id_', 'broadcast_th_', 'broadcast_vn_',
                    'broadcast_br_', 'broadcast_kr_', 'broadcast_ph_')
    search_fields = ['id', 'league', 'league_name', 'startdate']
    list_filter = ['league_name', 'startdate']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
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
@admin.register(SwipsFixturesInfo)
class SwipsFixturesInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'broadcast_id', 'broadcast_th', 'broadcast_vn',
                    'broadcast_br', 'broadcast_kr', 'broadcast_ph', 'ut')
    search_fields = ['id']
    list_filter = ['ut',]
    change_list_template = 'admin/steph_admin/change_list_custom.html'
