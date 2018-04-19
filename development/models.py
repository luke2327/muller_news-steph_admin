from django.db import models

# Create your models here.

class CurryAdBalance(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=8)
    weight = models.IntegerField()
    country_cd = models.CharField(max_length=2)
    os = models.CharField(max_length=7)
    valid_until = models.CharField(max_length=12)
    ut = models.DateTimeField()
    advertiser = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    ad_type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'curry_ad_balance'
        verbose_name = '광고 밸런스'
        verbose_name_plural = '광고 밸런스'
