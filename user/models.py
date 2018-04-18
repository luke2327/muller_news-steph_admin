from django.db import models

# Create your models here.
class SuUserFollowing(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    user_id = models.IntegerField()
    type = models.CharField(max_length=2)
    following = models.IntegerField()
    push_type = models.IntegerField()
    language = models.CharField(max_length=5)
    ut = models.DateTimeField()
    aws_subscription = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'su_user_following'
        unique_together = (('user_id', 'type', 'following', 'push_type'),)
