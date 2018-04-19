from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'name', 'tournament_stagefk', 'startdate',
                    'eventstatusfk', 'status_type', 'status_descfk', 'enetid',
                    'enetsportid', 'n', 'ut', 'locked')
    list_display_links = ['id',]

@admin.register(CurryFixturesInfo)
class CurryFixturesInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startdate', 'league', 'league_name',
                    'broadcast_id', 'broadcast_th', 'broadcast_vn',
                    'broadcast_br', 'broadcast_kr', 'broadcast_ph')
@admin.register(CurryMajorFixtures)
class CurryMajorFixturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'league', 'home_team', 'away_team',
                    'status_type', 'day', 'utc', 'kst')
