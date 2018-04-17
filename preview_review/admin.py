from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
# Register your models here.
from .models import *

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

class WPFixturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'match', 'tournament', 'league', 'round',\
            'team1', 'team2', 'startdate', 'p_type', 'status', 'pushed')

    list_editable = ['status', 'pushed']

class WpKeyPlAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'team', 'player', 'goals',\
            'assists', 'rating', 'played', 'n')
    list_editable = ['team', 'player', 'goals',\
            'assists', 'rating', 'played', 'n']

class WpTeamStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'team', 'rank', 'win', 'draw', 'defeit', 'pts',\
            'games', 'prev_rank', 'prev_result', 'goals', 'goals_re', 'ga_s', 'ga_s_re',\
            'ratings', 'ratings_re', 'n')
    list_editable = ['team', 'rank', 'win', 'draw', 'defeit', 'pts',\
            'games', 'prev_rank', 'prev_result', 'goals', 'goals_re', 'ga_s', 'ga_s_re',\
            'ratings', 'ratings_re', 'n']

class WpTopPlAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'team', 'player', 'stat_type', 'stat',\
            'avg_stat', 'n')
    list_editable = ['team', 'player', 'stat_type', 'stat',\
            'avg_stat', 'n']

class WpTransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'tournament', 'team', 'player', 'position', 'active',\
            'ut', 'del_field')
    list_editable = ['ut']

class SwipsReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'sport', 'league', 'result', 'ut', 'standing',\
            'startdate', 'ct', 'pushed')

class SwipsRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'player_id', 'type', 'rating', 'source')

class SwipsRatingPropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'mom_id', 'mom_goal', 'mom_assist', 'mom_min')

admin.site.register(WorldPeacePreview, WorldPeacePreviewAdmin)
admin.site.register(WpFixtures, WPFixturesAdmin)
admin.site.register(WpKeyPl, WpKeyPlAdmin)
admin.site.register(WpTeamStat, WpTeamStatAdmin)
admin.site.register(WpTopPl, WpTopPlAdmin)
admin.site.register(WpTransfer, WpTransferAdmin)
admin.site.register(SwipsReview, SwipsReviewAdmin)
admin.site.register(SwipsRating, SwipsRatingAdmin)
admin.site.register(SwipsRatingProperty, SwipsRatingPropertyAdmin)
