from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    enetid = models.PositiveIntegerField(db_column='enetID')  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    name_id = models.CharField(max_length=50, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    name_vi = models.CharField(max_length=50, blank=True, null=True)
    name_pt = models.CharField(max_length=50, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'
        verbose_name = '국가'
        verbose_name_plural = '국가'
