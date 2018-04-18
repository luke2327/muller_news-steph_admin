from django.db import models

# Create your models here.

class SwipsTransfer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    sport = models.IntegerField()
    player_id = models.IntegerField()
    player_name = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    from_team_id = models.IntegerField()
    from_team_name = models.CharField(max_length=45, blank=True, null=True)
    to_team_id = models.IntegerField()
    to_team_name = models.CharField(max_length=45, blank=True, null=True)
    is_loan = models.IntegerField()
    type = models.CharField(max_length=8)
    source_id = models.CharField(max_length=255, blank=True, null=True)
    source_th = models.CharField(max_length=255, blank=True, null=True)
    source_pt = models.CharField(max_length=255, blank=True, null=True)
    source_ko = models.CharField(max_length=255, blank=True, null=True)
    source_vi = models.CharField(max_length=255, blank=True, null=True)
    source_en = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()
    contract_dt = models.DateField()
    contract_info = models.CharField(max_length=8)
    fee = models.BigIntegerField()
    fee_info = models.CharField(max_length=8)
    fee_currency = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'swips_transfer'
        verbose_name = '이적'
        verbose_name_plural = '이적'
