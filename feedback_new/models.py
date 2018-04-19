from django.db import models

# Create your models here.

class SwipsQna(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    account_id = models.IntegerField()
    user_agent = models.CharField(max_length=255)
    language = models.CharField(max_length=32, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    img_ext = models.CharField(max_length=5, blank=True, null=True)
    img_rot = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    answer_ut = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    field_del = models.IntegerField(db_column='_del')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'swips_qna'
        verbose_name = '피드백'
        verbose_name_plural = '피드백'
