from django.db import models
# Create your models here.

class Event(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name='Match Id')
    name = models.CharField(max_length=150)
    tournament_stagefk = models.PositiveIntegerField(db_column='tournament_stageFK')  # Field name made lowercase.
    startdate = models.DateTimeField(blank=True, null=True)
    eventstatusfk = models.PositiveIntegerField(db_column='eventstatusFK')  # Field name made lowercase.
    status_type = models.CharField(max_length=11)
    status_descfk = models.PositiveIntegerField(db_column='status_descFK')  # Field name made lowercase.
    enetid = models.IntegerField(db_column='enetID')  # Field name made lowercase.
    enetsportid = models.CharField(db_column='enetSportID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    locked = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'event'
        verbose_name = '경기'
        verbose_name_plural = '경기'

class CurryFixturesInfo(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name='Match Id')
    name = models.CharField(max_length=150)
    startdate = models.DateTimeField()
    league = models.PositiveIntegerField()
    league_name = models.CharField(max_length=30)
    broadcast_id = models.CharField(max_length=50, blank=True, null=True)
    broadcast_th = models.CharField(max_length=50, blank=True, null=True)
    broadcast_vn = models.CharField(max_length=50, blank=True, null=True)
    broadcast_br = models.CharField(max_length=50, blank=True, null=True)
    broadcast_kr = models.CharField(max_length=50, blank=True, null=True)
    broadcast_ph = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_fixtures_info'
        verbose_name = '중계정보입력'
        verbose_name_plural = '중계정보입력'

class CurryMajorFixtures(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name='Match Id')
    league = models.CharField(max_length=30)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    status_type = models.CharField(max_length=20)
    day = models.CharField(max_length=1)
    utc = models.CharField(max_length=12)
    kst = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'curry_major_fixtures'
        verbose_name = '주요경기조회'
        verbose_name_plural = '주요경기조회'

class SwipsFixturesInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    broadcast_id = models.CharField(max_length=50, blank=True, null=True)
    broadcast_th = models.CharField(max_length=50, blank=True, null=True)
    broadcast_vn = models.CharField(max_length=50, blank=True, null=True)
    broadcast_br = models.CharField(max_length=50, blank=True, null=True)
    broadcast_kr = models.CharField(max_length=50, blank=True, null=True)
    broadcast_ph = models.CharField(max_length=50, blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_fixtures_info'
        verbose_name = '중계정보조회'
        verbose_name_plural = '중계정보조회'
