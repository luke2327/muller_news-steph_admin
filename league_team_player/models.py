from django.db import models

# Create your models here.
class SwipsPlayerInfo(models.Model):
    player = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    mid_name_ko = models.CharField(max_length=30, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    mid_name_th = models.CharField(max_length=30, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    draft = models.CharField(max_length=30, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_player_info'
        verbose_name = '선수'
        verbose_name_plural = '선수'

class SwipsTeamInfo(models.Model):
    team = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    short_name = models.CharField(max_length=5, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    mid_name_ko = models.CharField(max_length=30, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    mid_name_th = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)
    last_rank = models.CharField(max_length=30, blank=True, null=True)
    no_champions = models.IntegerField(blank=True, null=True)
    manager = models.CharField(max_length=50, blank=True, null=True)
    manager_ko = models.CharField(max_length=50, blank=True, null=True)
    manager_th = models.CharField(max_length=50, blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    social_ko = models.CharField(max_length=255, blank=True, null=True)
    social_pt = models.CharField(max_length=255, blank=True, null=True)
    social_id = models.CharField(max_length=255, blank=True, null=True)
    social_th = models.CharField(max_length=255, blank=True, null=True)
    social_vi = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_team_info'
        verbose_name = '팀'
        verbose_name_plural = '팀'

class SwipsLeagueInfo(models.Model):
    league = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    short_name = models.CharField(max_length=6, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    name_pt = models.CharField(max_length=50, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    name_id = models.CharField(max_length=50, blank=True, null=True)
    name_vi = models.CharField(max_length=50, blank=True, null=True)
    no_teams = models.IntegerField(blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)
    last_champion = models.IntegerField(blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    social_ko = models.CharField(max_length=255, blank=True, null=True)
    social_pt = models.CharField(max_length=255, blank=True, null=True)
    social_id = models.CharField(max_length=255, blank=True, null=True)
    social_th = models.CharField(max_length=255, blank=True, null=True)
    social_vi = models.CharField(max_length=255, blank=True, null=True)
    social_en = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=6, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=20, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_league_info'
        verbose_name = '리그'
        verbose_name_plural = '리그'

class CurryPlayer(models.Model):
    # id = models.IntegerField(primary_key=True)
    player = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    mid_name_ko = models.CharField(max_length=30, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    mid_name_th = models.CharField(max_length=30, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    draft = models.CharField(max_length=30, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    ut = models.DateTimeField()
    position = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_player'
        verbose_name = '중복 선수 확인'
        verbose_name_plural = '중복 선수 확인'
class SwipsPlayerCareer(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    date_from = models.CharField(max_length=12, blank=True, null=True)
    date_to = models.CharField(max_length=12, blank=True, null=True)
    active = models.CharField(max_length=5, blank=True, null=True)
    ut = models.CharField(max_length=12, blank=True, null=True)
    on_loan = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_player_career'
        verbose_name = '선수 커리어'
        verbose_name_plural = '선수 커리어'
