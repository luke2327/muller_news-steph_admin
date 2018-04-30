from django.db import models
class WorldPeacePorView(models.Model):
    id = models.AutoField(primary_key=True)
    round = models.IntegerField(blank=True)
    tournament = models.IntegerField(blank=True, null=True)
    league = models.IntegerField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    lineup_type = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_peace_por_view'
        verbose_name = '베스트11'
        verbose_name_plural = '베스트11'
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
    id = models.AutoField(primary_key=True)
    match = models.IntegerField(blank=True, help_text="경기 아이디")
    tournament = models.IntegerField(blank=True, null=True, help_text="토너먼트 아이디")
    league = models.IntegerField(blank=True, null=True, help_text="리그 아이디")
    round = models.IntegerField(blank=True, null=True, help_text="리그 라운드")
    team1 = models.IntegerField(blank=True, null=True, help_text="홈팀")
    team2 = models.IntegerField(blank=True, null=True, help_text="어웨이팀")
    startdate = models.DateTimeField(blank=True, null=True, help_text="경기 시작시각")
    p_type = models.IntegerField(blank=True, null=True, help_text="0 : 1라운드 1:2~5라운드 2: 6라운드이상")
    status = models.CharField(max_length=9, help_text="ready, confirmed")
    pushed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_fixtures'
        verbose_name = '인앱 프리뷰 Fixtures(raw)'
        verbose_name_plural = '인앱 프리뷰 Fixtures(raw)'


class WpInjuries(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    match_id = models.IntegerField(help_text="경기 아이디")
    team = models.IntegerField(help_text="팀 아이디")
    player = models.IntegerField(help_text="선수 아이디")
    goals = models.IntegerField(help_text="최근 골수")
    assists = models.IntegerField(help_text="최근 어시스트 수")
    rating = models.FloatField(help_text="최근 평점평균")
    played = models.IntegerField(help_text="최근 뛴 경기수")
    n = models.IntegerField(help_text="")

    class Meta:
        managed = False
        db_table = 'wp_key_pl'
        unique_together = (('match_id', 'team'),)
        verbose_name = '인앱 프리뷰 키플레이어(raw)'
        verbose_name_plural = '인앱 프리뷰 키플레이어(raw)'


class WpTeamStat(models.Model):
    id = models.AutoField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True, help_text="경기 아이디")
    team = models.IntegerField(blank=True, null=True, help_text="팀 아이디")
    rank = models.IntegerField(blank=True, null=True, help_text="팀 현재 순위")
    win = models.IntegerField(blank=True, null=True, help_text="승")
    draw = models.IntegerField(blank=True, null=True, help_text="무")
    defeit = models.IntegerField(blank=True, null=True, help_text="패")
    pts = models.IntegerField(blank=True, null=True, help_text="승점")
    games = models.IntegerField(blank=True, null=True, help_text="경기수")
    prev_rank = models.CharField(max_length=32, blank=True, null=True, help_text="이전순위변화")
    prev_result = models.CharField(max_length=32, blank=True, null=True, help_text="이전 결과 변화(1:home lose, 2:home draw, 3:homewin 4:awaylose 5:awaydraw 6:awaywin")
    goals = models.IntegerField(blank=True, null=True, help_text="총 골수")
    goals_re = models.FloatField(blank=True, null=True, help_text="최근경기 평균골수")
    ga_s = models.IntegerField(blank=True, null=True, help_text="총 실점수")
    ga_s_re = models.FloatField(blank=True, null=True, help_text="최근경기 평균실점")
    ratings = models.FloatField(blank=True, null=True, help_text="총 평점합")
    ratings_re = models.FloatField(blank=True, null=True, help_text="최근경기 평점평균")
    n = models.IntegerField(blank=True, null=True, help_text="")

    class Meta:
        managed = False
        db_table = 'wp_team_stat'
        unique_together = (('match_id', 'team'),)
        verbose_name = '인앱 프리뷰 팀 스탯(raw)'
        verbose_name_plural = '인앱 프리뷰 팀 스탯(raw)'


class WpTopPl(models.Model):
    id = models.AutoField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True, help_text="경기 아이디")
    team = models.IntegerField(blank=True, null=True, help_text="팀 아이디")
    player = models.IntegerField(blank=True, null=True, help_text="선수 아이디")
    stat_type = models.CharField(max_length=7, blank=True, null=True, help_text="goals, assists, ycards, rating, p_time")
    stat = models.FloatField(blank=True, null=True, help_text="stat_type 에 대응하는 시즌 기록")
    avg_stat = models.FloatField(blank=True, null=True, help_text="stat 값의 시간당 환산값(preview에 보여지는값기준)")
    n = models.IntegerField(blank=True, null=True, help_text="preview상 보여지는 순서")

    class Meta:
        managed = False
        db_table = 'wp_top_pl'
        unique_together = (('match_id', 'team', 'stat_type'),)
        verbose_name = '인앱 프리뷰 탑플레이어(raw)'
        verbose_name_plural = '인앱 프리뷰 탑플레이어(raw)'


class WpTransfer(models.Model):
    id = models.AutoField(primary_key=True)
    tournament = models.IntegerField(blank=True, null=True, help_text="토너먼트 아이디(년도마다 다름)")
    team = models.IntegerField(blank=True, null=True, help_text="팀 아이디")
    player = models.IntegerField(blank=True, null=True, help_text="선수 아이디")
    position = models.CharField(max_length=10, blank=True, null=True, help_text="선수 포지션")
    active = models.CharField(max_length=3, blank=True, null=True, help_text="yes 이면 transfer in no 이면 transfer out")
    ut = models.CharField(max_length=20,blank=True, null=True, help_text="이적 시점(이넷펄스에서 주는 값)")
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'wp_transfer'
        unique_together = (('team', 'player', 'ut'),)
        verbose_name = '인앱 프리뷰 이적(raw)'
        verbose_name_plural = '인앱 프리뷰 이적(raw)'

class SwipsReview(models.Model):
    id = models.AutoField(primary_key=True)
    sport = models.IntegerField(help_text="")
    league = models.IntegerField(help_text="")
    result = models.TextField(blank=True, null=True)
    ut = models.DateTimeField(help_text="최근 review update된 시간")
    standing = models.TextField(blank=True, null=True, help_text="")
    startdate = models.DateTimeField(help_text="경기 시작 시간")
    ct = models.DateTimeField(help_text="처음 review가 만들어진 시간; 앱에 표기되는 시간")
    pushed = models.IntegerField(help_text="푸시 나간 횟수")

    class Meta:
        managed = False
        db_table = 'swips_review'
        verbose_name = '리뷰(raw)'
        verbose_name_plural = '리뷰(raw)'

class SwipsRating(models.Model):
    id = models.AutoField(primary_key=True)
    match_id = models.IntegerField(help_text="매치 id")
    player_id = models.IntegerField(help_text="선수 id")
    type = models.IntegerField(help_text="1: 스타팅home, 2:스타팅away, 3: Sub home, 4: Sub away")
    rating = models.FloatField(help_text="평점")
    source = models.CharField(max_length=45, help_text="평점 소스")

    class Meta:
        managed = False
        db_table = 'swips_rating'
        unique_together = (('match_id', 'player_id', 'source'),)
        verbose_name = '리뷰 Rating(raw)'
        verbose_name_plural = '리뷰 Rating(raw)'


class SwipsRatingProperty(models.Model):
    id = models.AutoField(primary_key=True, help_text=u"매치 id")
    mom_id = models.IntegerField(blank=True, null=True, help_text=u"선수 id")
    mom_goal = models.IntegerField(blank=True, null=True)
    mom_assist = models.IntegerField(blank=True, null=True)
    mom_min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_rating_property'
        verbose_name = '리뷰 MOM(raw)'
        verbose_name_plural = '리뷰 MOM(raw)'
