from django.db import models

# Create your models here.

class CurryExposePostLog(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    target = models.ForeignKey('CurryExposeTarget', models.DO_NOTHING, db_column='target')
    user = models.CharField(max_length=45)
    desc = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'curry_expose_post_log'
        verbose_name = '작성글 Log'
        verbose_name_plural = '작성글 Log'


class CurryExposeTarget(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'curry_expose_target'
        verbose_name = '점령지 List'
        verbose_name_plural = '점령지 List'
