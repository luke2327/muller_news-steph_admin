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

class SwipsMatchDetailCustom(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    match_id = models.IntegerField()
    team_id = models.IntegerField()
    lineup_number = models.IntegerField(blank=True, null=True)
    shirt_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=45)
    type = models.IntegerField()
    minute = models.IntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_match_detail_custom'
        unique_together = (('match_id', 'team_id', 'name', 'type', 'minute'),)
