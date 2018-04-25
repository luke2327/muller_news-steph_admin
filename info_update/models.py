from django.db import models

# Create your models here.

class CurryInfoDbModify(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.IntegerField()
    type = models.CharField(max_length=2)
    migrate_item = models.IntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    valid_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_info_db_modify'
        verbose_name = '앱 DB 변경'
        verbose_name_plural = '앱 DB 변경'


class CurryInfoImageModify(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.IntegerField()
    type = models.CharField(max_length=2)
    desc = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    valid_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_info_image_modify'
        verbose_name = '이미지 변경'
        verbose_name_plural = '이미지 변경'
