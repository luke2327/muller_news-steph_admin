from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'name', 'tournament_stagefk', 'startdate',
                    'eventstatusfk', 'status_type', 'status_descfk', 'enetid',
                    'enetsportid', 'n', 'ut', 'locked')
    list_display_links = ['id',]
    list_filter = ['status_type',]
    search_fields = ['name', 'id',]

@admin.register(CurryFixturesInfo)
class CurryFixturesInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startdate', 'league', 'league_name',
                    'broadcast_id', 'broadcast_th', 'broadcast_vn',
                    'broadcast_br', 'broadcast_kr', 'broadcast_ph')
    search_fields = ['id', 'league',]
    list_editable = ['broadcast_id', 'broadcast_th', 'broadcast_vn',
                    'broadcast_br', 'broadcast_kr', 'broadcast_ph']


@admin.register(CurryMajorFixtures)
class CurryMajorFixturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'league', 'home_team', 'away_team',
                    'status_type', 'day', 'utc', 'kst')
<<<<<<< HEAD
    search_fields = ['id','league', 'home_team', 'away_team']
    list_filter = ['league',]

=======
>>>>>>> f6e30a3e535bf5217d9c524b5ea38a859ae47fc2
@admin.register(SwipsFixturesInfo)
class SwipsFixturesInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'broadcast_id', 'broadcast_th', 'broadcast_vn',
                    'broadcast_br', 'broadcast_kr', 'broadcast_ph', 'ut')
<<<<<<< HEAD
    search_fields = ['id']
=======
>>>>>>> f6e30a3e535bf5217d9c524b5ea38a859ae47fc2
