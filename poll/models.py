from django.db import models

# Create your models here.

class SwipsPoll(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.IntegerField()
    number = models.IntegerField()
    type = models.CharField(max_length=2, blank=True, null=True)
    participant = models.IntegerField(blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_poll'
        unique_together = (('type', 'participant', 'item'),)
        verbose_name = '투표'
        verbose_name_plural = '투표'

class SwipsBoard(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=2)
    participant = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=2)
    text = models.TextField(blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_board'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'
