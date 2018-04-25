from django.db import models

# Create your models here.
##
class SuUserFollowing(models.Model):
    id = models.AutoField(primary_key=True)
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
        verbose_name = '사용자 팔로잉'
        verbose_name_plural = '사용자 팔로잉'

class SuAccountFollowing(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    type = models.CharField(max_length=2)
    following = models.IntegerField()
    push_type = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'su_account_following'
        unique_together = (('account_id', 'type', 'following', 'push_type'),)
        verbose_name = '계정 팔로잉'
        verbose_name_plural = '계정 팔로잉'

class SuTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    account_id = models.IntegerField()
    login_ut = models.DateTimeField(blank=True, null=True)
    logout_ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'su_transaction'
        unique_together = (('user_id', 'account_id', 'login_ut'),)
        verbose_name = '트랜젝션'
        verbose_name_plural = '트랜젝션'

class SuAccount(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    pf = models.CharField(max_length=8, blank=True, null=True)
    pf_user_id = models.CharField(max_length=50, blank=True, null=True)
    pf_user_name = models.CharField(max_length=64, blank=True, null=True)
    pf_user_token = models.CharField(max_length=2048, blank=True, null=True)
    pf_image_url = models.CharField(max_length=255, blank=True, null=True)
    email_confirmed = models.CharField(max_length=3, blank=True, null=True)
    secret_key = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'su_account'
        unique_together = (('pf', 'pf_user_id'),)
        verbose_name = '계정'
        verbose_name_plural = '계정'

class SuUser(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=25, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    push_key = models.CharField(max_length=1023, blank=True, null=True)
    aws_endpoint = models.CharField(max_length=255, blank=True, null=True)
    last_login_ut = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'su_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
