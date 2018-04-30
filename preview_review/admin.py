from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
# Register your models here.
from .models import *
from steph.util.util import Util
from django.utils.html import format_html

class WorldPeacePorViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'round', 'tournament', 'league',\
            'player', 'lineup_type', 'position', 'rating',\
            'team_')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_filter = ['id', 'round', 'league']
    search_fields = ['id', 'round', 'tournament', 'league',\
            'player', 'lineup_type', 'position', 'rating',\
            'team_']
    def team_(self, obj):
        return Util().get_popover_best11('admin', 'world_peace_por', 'id', obj.id,\
                           'team', obj.team, 'text', obj.tournament, obj.round)
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True

class WorldPeacePreviewAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'league', 'team1', 'team2',\
            'match_date', 'team1_rank', 'team2_rank', 'team1_win', 'team2_win',\
            'team1_draw', 'team2_draw', 'team1_defeit', 'team2_defeit',\
            'team1_pts', 'team2_pts', 'team1_result', 'team2_result',\
            'team1_goals_per_game', 'team2_goals_per_game',\
            'team1_goals_per_game_5', 'team2_goals_per_game_5',\
            'team1_goals_against_per_game', 'team2_goals_against_per_game',\
            'team1_goals_against_per_game_5', 'team2_goals_against_per_game_5',\
            'team1_key_player', 'team2_key_player',\
            'team1_key_player_goal', 'team2_key_player_goal',\
            'team1_key_player_assist', 'team2_key_player_assist',\
            'team1_top_player', 'team2_top_player',\
            'team1_top_player_stat', 'team2_top_player_stat',\
            'team1_top_player_stat_per', 'team2_top_player_stat_per',\
            'team1_injuries', 'team2_injuries',\
            'status', 'type')
    list_editable = ['league', 'team1', 'team2',\
            'match_date', 'team1_rank', 'team2_rank', 'team1_win', 'team2_win',\
            'team1_draw', 'team2_draw', 'team1_defeit', 'team2_defeit',\
            'team1_pts', 'team2_pts', 'team1_result', 'team2_result',\
            'team1_goals_per_game', 'team2_goals_per_game',\
            'team1_goals_per_game_5', 'team2_goals_per_game_5',\
            'team1_goals_against_per_game', 'team2_goals_against_per_game',\
            'team1_goals_against_per_game_5', 'team2_goals_against_per_game_5',\
            'team1_key_player', 'team2_key_player',\
            'team1_key_player_goal', 'team2_key_player_goal',\
            'team1_key_player_assist', 'team2_key_player_assist',\
            'team1_top_player', 'team2_top_player',\
            'team1_top_player_stat', 'team2_top_player_stat',\
            'team1_top_player_stat_per', 'team2_top_player_stat_per',\
            'team1_injuries', 'team2_injuries',\
            'status', 'type']
    ordering = ['-match_date']
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
class WPFixturesAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'match', 'tournament', 'league', 'round',\
            'team1', 'team2', 'startdate', 'p_type', 'status', 'pushed')

    ordering = ['-startdate']
    list_filter = ['id', 'match', 'tournament',
                  'league', 'round', 'team1', 'team2',
                  'startdate', 'p_type', 'status']
    search_fields = ['id', 'match', 'tournament',
                  'league', 'round', 'team1', 'team2',
                  'startdate', 'p_type', 'status']
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
class WpKeyPlAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'match_id', 'team', 'player', 'goals',\
            'assists', 'rating', 'played', 'n')
    list_filter = ['id', 'match_id', 'team', 'player',
                      'goals', 'assists', 'rating', 'played', 'n']
    search_fields = ['id', 'match_id', 'team', 'player',
                      'goals', 'assists', 'rating', 'played', 'n']
    ordering = ['-match_id']
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
class WpTeamStatAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'match_id', 'team', 'rank', 'win', 'draw', 'defeit', 'pts',\
            'games', 'prev_rank', 'prev_result', 'goals', 'goals_re', 'ga_s', 'ga_s_re',\
            'ratings', 'ratings_re', 'n')
    list_filter = ['id', 'match_id', 'team', 'rank', 'win',
                      'draw', 'defeit', 'pts', 'games', 'prev_rank',
                      'prev_result', 'goals', 'goals_re', 'ga_s',
                      'ga_s_re', 'ratings', 'ratings_re', 'n']
    search_fields = ['id', 'match_id', 'team', 'rank', 'win',
                      'draw', 'defeit', 'pts', 'games', 'prev_rank',
                      'prev_result', 'goals', 'goals_re', 'ga_s',
                      'ga_s_re', 'ratings', 'ratings_re', 'n']
    ordering = ['-match_id']
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
class WpTopPlAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'match_id', 'team', 'player', 'stat_type', 'stat',\
            'avg_stat', 'n')
    list_filter = ['id', 'match_id', 'team', 'player',
                      'stat_type', 'stat', 'avg_stat', 'n']
    search_fields = ['id', 'match_id', 'team', 'player',
                      'stat_type', 'stat', 'avg_stat', 'n']
    ordering = ['-match_id']
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return False
class WpTransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'tournament', 'team', 'player', 'position', 'active',\
            'ut', 'del_field')
    list_filter = ['id', 'tournament', 'team', 'player', 'position',
                   'active', 'ut', 'del_field']
    search_fields = ['id', 'tournament', 'team', 'player', 'position',
                   'active', 'ut', 'del_field']
    def has_delete_permission(self, request, obj=None):
         return True
class SwipsReviewAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'sport', 'league', 'result', 'ut', 'standing',\
            'startdate', 'ct', 'pushed')
    list_filter = ['id', 'league', 'ut', 'startdate', 'ct', 'pushed']
    search_fields = ['id', 'league', 'ut', 'startdate', 'ct', 'pushed']
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
         return True
class SwipsRatingAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'match_id', 'player_id', 'type', 'rating', 'source')
    list_filter = ['match_id', 'type', 'source']
    search_fields = ['match_id', 'type', 'rating', 'source']
class SwipsRatingPropertyAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'mom_id', 'mom_goal', 'mom_assist', 'mom_min')
    list_filter = ['mom_id',]
    search_fields = ['id', 'mom_id']

admin.site.register(WorldPeacePorView, WorldPeacePorViewAdmin)
admin.site.register(WorldPeacePreview, WorldPeacePreviewAdmin)
admin.site.register(WpFixtures, WPFixturesAdmin)
admin.site.register(WpKeyPl, WpKeyPlAdmin)
admin.site.register(WpTeamStat, WpTeamStatAdmin)
admin.site.register(WpTopPl, WpTopPlAdmin)
admin.site.register(WpTransfer, WpTransferAdmin)
admin.site.register(SwipsReview, SwipsReviewAdmin)
admin.site.register(SwipsRating, SwipsRatingAdmin)
admin.site.register(SwipsRatingProperty, SwipsRatingPropertyAdmin)
