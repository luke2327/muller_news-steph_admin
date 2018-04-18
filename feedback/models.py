from django.db import models

# Create your models here.

class SwipsFeedback(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    user_id = models.IntegerField()
    user_agent = models.CharField(max_length=255)
    language = models.CharField(max_length=10, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    email = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_feedback'
        verbose_name = '피드백'
        verbose_name_plural = '피드백'
