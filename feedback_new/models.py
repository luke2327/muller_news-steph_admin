from django.db import models

# Create your models here.
import datetime
class SwipsQna(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(help_text="anom id")
    account_id = models.IntegerField(help_text="swips account id")
    user_agent = models.CharField(max_length=255)
    language = models.CharField(max_length=32, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True, help_text="피드백")
    img_ext = models.CharField(max_length=5, blank=True, null=True)
    img_rot = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True, help_text="답글")
    ut = models.DateTimeField(blank=True, null=True, help_text="피드백 올라온 시각")
    answer_ut = models.TextField(blank=True, null=True, help_text="답글 단 시각")
    status = models.CharField(max_length=9, blank=True, null=True, help_text="ready : 답글X answered : 답글 O")
    field_del = models.IntegerField(db_column='_del')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'swips_qna'
        verbose_name = '피드백'
        verbose_name_plural = '피드백'
