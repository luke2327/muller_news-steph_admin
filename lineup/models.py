from django.db import models
class SwipsLineupCustom(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField()
    team = models.IntegerField()
    lineup_number = models.IntegerField(blank=True, null=True)
    shirt_number = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=45)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_lineup_custom'
        unique_together = (('match_id', 'team', 'lineup_number'),)
        verbose_name = '라인업 수동입력'
        verbose_name_plural = '라인업 수동입력'

class SwipsMatchDetailCustom(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    match_id = models.IntegerField(help_text="매치 id")
    team_id = models.IntegerField(help_text="팀 id")
    lineup_number = models.IntegerField(blank=True, null=True, help_text="1~11 선발, 12~ 교체명단")
    shirt_number = models.IntegerField(blank=True, null=True, help_text="백넘버")
    name = models.CharField(max_length=45, help_text="선수 이름")
    type = models.IntegerField(help_text="매치팩트 타입\n7:골, 14:옐로, 16:레드, 20:교체아웃, 32:교체인")
    minute = models.IntegerField(help_text="경기중 시간. 인저리타임은 45/90으로 표기")
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_match_detail_custom'
        unique_together = (('match_id', 'team_id', 'name', 'type', 'minute'),)
        verbose_name = '매치팩트 수동입력'
        verbose_name_plural = '매치팩트 수동입력'
