from django.db import models

# Create your models here.
class SwipsBoardLike(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=2)
    root_id = models.IntegerField()
    account_id = models.IntegerField()
    account_type = models.CharField(max_length=5)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_board_like'
        unique_together = (('type', 'root_id', 'account_id'),)
        verbose_name = '좋아요'
        verbose_name_plural = '좋아요'


class SwipsBoardLikeDev(models.Model):
    type = models.CharField(max_length=2)
    root_id = models.IntegerField()
    account_id = models.IntegerField()
    account_type = models.CharField(max_length=5)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_board_like_dev'
        unique_together = (('type', 'root_id', 'account_id'),)


class SwipsBoardPost(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=2)
    participant = models.IntegerField()
    language = models.CharField(max_length=2, blank=True, null=True)
    account_id = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    like = models.IntegerField()
    img_ext = models.CharField(max_length=5, blank=True, null=True)
    img_rot = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)
    top = models.IntegerField()
    create_time = models.CharField(max_length=10)
    edit_time = models.CharField(max_length=10)
    top_time = models.CharField(max_length=10)
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'swips_board_post'
        verbose_name_plural = '게시판'
        verbose_name = '게시판'


class SwipsBoardPostDev(models.Model):
    type = models.CharField(max_length=2)
    participant = models.IntegerField()
    language = models.CharField(max_length=2, blank=True, null=True)
    account_id = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    like = models.IntegerField()
    img_ext = models.CharField(max_length=5, blank=True, null=True)
    img_rot = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)
    top = models.IntegerField()
    create_time = models.DateTimeField()
    edit_time = models.DateTimeField()
    top_time = models.DateTimeField()
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'swips_board_post_dev'


class SwipsBoardReply(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=2)
    participant = models.IntegerField()
    account_id = models.IntegerField()
    post_id = models.IntegerField()
    root_type = models.IntegerField()
    root_id = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    create_time = models.CharField(max_length=10)
    edit_time = models.CharField(max_length=10)
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.
    language = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_board_reply'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'


class SwipsBoardReplyDev(models.Model):
    type = models.CharField(max_length=2)
    participant = models.IntegerField()
    account_id = models.IntegerField()
    post_id = models.IntegerField()
    root_type = models.IntegerField()
    root_id = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    edit_time = models.DateTimeField()
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.
    language = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_board_reply_dev'
