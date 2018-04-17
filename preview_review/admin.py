from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
# Register your models here.
from .models import *

class WorldPeacePreviewAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'match_info', 'league', 'team1', 'team2',\
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
    list_editable = ['match_info', 'league', 'team1', 'team2',\
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

admin.site.register(WorldPeacePreview, WorldPeacePreviewAdmin)
