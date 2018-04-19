from django.db import models

# Create your models here.
class WorldPeacePreview(models.Model):
    match_id = models.IntegerField(primary_key=True)
    match_info = models.CharField(max_length=45, blank=True, null=True)
    team1 = models.IntegerField(blank=True, null=True)
    team2 = models.IntegerField(blank=True, null=True)
    match_date = models.DateTimeField(blank=True, null=True)
    team1_rank = models.CharField(max_length=45, blank=True, null=True)
    team2_rank = models.CharField(max_length=45, blank=True, null=True)
    team1_win = models.IntegerField(blank=True, null=True)
    team2_win = models.IntegerField(blank=True, null=True)
    team1_draw = models.IntegerField(blank=True, null=True)
    team2_draw = models.IntegerField(blank=True, null=True)
    team1_defeit = models.IntegerField(blank=True, null=True)
    team2_defeit = models.IntegerField(blank=True, null=True)
    team1_pts = models.IntegerField(blank=True, null=True)
    team2_pts = models.IntegerField(blank=True, null=True)
    team1_result = models.CharField(max_length=45, blank=True, null=True)
    team2_result = models.CharField(max_length=45, blank=True, null=True)
    team1_goals_per_game = models.FloatField(blank=True, null=True)
    team2_goals_per_game = models.FloatField(blank=True, null=True)
    team1_goals_per_game_5 = models.FloatField(blank=True, null=True)
    team2_goals_per_game_5 = models.FloatField(blank=True, null=True)
    team1_goals_against_per_game = models.FloatField(blank=True, null=True)
    team2_goals_against_per_game = models.FloatField(blank=True, null=True)
    team1_goals_against_per_game_5 = models.FloatField(blank=True, null=True)
    team2_goals_against_per_game_5 = models.FloatField(blank=True, null=True)
    team1_key_player = models.IntegerField(blank=True, null=True)
    team2_key_player = models.IntegerField(blank=True, null=True)
    team1_key_player_goal = models.IntegerField(blank=True, null=True)
    team2_key_player_goal = models.IntegerField(blank=True, null=True)
    team1_key_player_assist = models.IntegerField(blank=True, null=True)
    team2_key_player_assist = models.IntegerField(blank=True, null=True)
    team1_top_player = models.CharField(max_length=45, blank=True, null=True)
    team2_top_player = models.CharField(max_length=45, blank=True, null=True)
    team1_top_player_stat = models.CharField(max_length=45, blank=True, null=True)
    team2_top_player_stat = models.CharField(max_length=45, blank=True, null=True)
    team1_top_player_stat_per = models.CharField(max_length=45, blank=True, null=True)
    team2_top_player_stat_per = models.CharField(max_length=45, blank=True, null=True)
    team1_injuries = models.CharField(max_length=45, blank=True, null=True)
    team2_injuries = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=9)
    type = models.IntegerField()
    league = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'world_peace_preview'
        verbose_name = '웹 프리뷰'
        verbose_name_plural = '웹 프리뷰'

class WpFixtures(models.Model):
    id = models.IntegerField(primary_key=True)
    match = models.IntegerField(unique=True, blank=True, null=True)
    tournament = models.IntegerField(blank=True, null=True)
    league = models.IntegerField(blank=True, null=True)
    round = models.IntegerField(blank=True, null=True)
    team1 = models.IntegerField(blank=True, null=True)
    team2 = models.IntegerField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    p_type = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=9)
    pushed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_fixtures'
        verbose_name = '인앱 프리뷰 Fixtures(raw)'
        verbose_name_plural = '인앱 프리뷰 Fixtures(raw)'


class WpInjuries(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.IntegerField(blank=True, null=True)
    match = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_injuries'
        unique_together = (('player', 'match', 'team'),)
        verbose_name = '인앱 프리뷰 부상자명단(raw)'
        verbose_name_plural = '인앱 프리뷰 부상자 명단(raw)'


class WpKeyPl(models.Model):
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField()
    team = models.IntegerField()
    player = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    rating = models.FloatField()
    played = models.IntegerField()
    n = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_key_pl'
        unique_together = (('match_id', 'team'),)
        verbose_name = '인앱 프리뷰 키플레이어(raw)'
        verbose_name_plural = '인앱 프리뷰 키플레이어(raw)'


class WpTeamStat(models.Model):
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    draw = models.IntegerField(blank=True, null=True)
    defeit = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    games = models.IntegerField(blank=True, null=True)
    prev_rank = models.CharField(max_length=32, blank=True, null=True)
    prev_result = models.CharField(max_length=32, blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    goals_re = models.FloatField(blank=True, null=True)
    ga_s = models.IntegerField(blank=True, null=True)
    ga_s_re = models.FloatField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    ratings_re = models.FloatField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_team_stat'
        unique_together = (('match_id', 'team'),)
        verbose_name = '인앱 프리뷰 팀 스탯(raw)'
        verbose_name_plural = '인앱 프리뷰 팀 스탯(raw)'


class WpTopPl(models.Model):
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    stat_type = models.CharField(max_length=7, blank=True, null=True)
    stat = models.FloatField(blank=True, null=True)
    avg_stat = models.FloatField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_top_pl'
        unique_together = (('match_id', 'team', 'stat_type'),)
        verbose_name = '인앱 프리뷰 탑플레이어(raw)'
        verbose_name_plural = '인앱 프리뷰 탑플레이어(raw)'


class WpTransfer(models.Model):
    id = models.IntegerField(primary_key=True)
    tournament = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    active = models.CharField(max_length=3, blank=True, null=True)
    ut = models.CharField(max_length=20,blank=True, null=True)
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'wp_transfer'
        unique_together = (('team', 'player', 'ut'),)
        verbose_name = '인앱 프리뷰 이적(raw)'
        verbose_name_plural = '인앱 프리뷰 이적(raw)'

class SwipsReview(models.Model):
    id = models.IntegerField(primary_key=True)
    sport = models.IntegerField()
    league = models.IntegerField()
    result = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    standing = models.TextField(blank=True, null=True)
    startdate = models.DateTimeField()
    ct = models.DateTimeField()
    pushed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'swips_review'
        verbose_name = '리뷰(raw)'
        verbose_name_plural = '리뷰(raw)'

class SwipsRating(models.Model):
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField()
    player_id = models.IntegerField()
    type = models.IntegerField()
    rating = models.FloatField()
    source = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'swips_rating'
        unique_together = (('match_id', 'player_id', 'source'),)
        verbose_name = '리뷰 Rating(raw)'
        verbose_name_plural = '리뷰 Rating(raw)'


class SwipsRatingProperty(models.Model):
    id = models.IntegerField(primary_key=True)
    mom_id = models.IntegerField(blank=True, null=True)
    mom_goal = models.IntegerField(blank=True, null=True)
    mom_assist = models.IntegerField(blank=True, null=True)
    mom_min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_rating_property'
        verbose_name = '리뷰 MOM(raw)'
        verbose_name_plural = '리뷰 MOM(raw)'
