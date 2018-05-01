from django.db import models

# Create your models here.

class CurryAdBalance(models.Model):
    type_choice = (
        ('admob','admob'),
        ('mobvista','mobvista'),
        ('direct','direct'),
    )
    ad_type_choice = (
        ('native_m','native_m'),
        ('native_s','native_s'),
        ('banner','banner'),
        ('native_b','native_b'),
    )
    yes_no = (
        ('yes', 'yes'),
        ('no', 'no')
    )

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=8, choices = type_choice, help_text="직접광고는 direct")
    weight = models.IntegerField(help_text="광고의 노출 빈도; admob/mobvista의 경우 0이어야함, direct일 경우는 0이 아니여야함")
    country_cd = models.CharField(max_length=2, help_text="영문 대문자 2자리 입력")
    os = models.CharField(max_length=7, help_text='"android" 또는 "ios"')
    valid_until = models.DateTimeField(blank=True, null=True, help_text="광고가 끝나는 시점. UTC기준")
    ut = models.DateTimeField(blank=True, null=True)
    advertiser = models.CharField(max_length=45, blank=True, null=True, help_text="direct의 경우에만 입력. 임의의 입력")
    link = models.CharField(max_length=255, blank=True, null=True, help_text="direct의 경우에만 입력. 연결될 링크")
    image_link = models.CharField(max_length=255, blank=True, null=True, help_text="direct의 경우에만 입력. 이미지 주소")
    ad_type = models.CharField(max_length=8, choices = ad_type_choice, help_text='"native_m" or "native_s" or "banner"')
    client_version = models.IntegerField(help_text="해당 광고를 노출할 버전 ex)1.2.3 -> 1002003")
    include_lower_versions = models.CharField(max_length=3, choices = yes_no, help_text="client_version을 포함하여 과거버전을 포함시킬지 여부")
    include_upper_versions = models.CharField(max_length=3, choices = yes_no, help_text="client_version을 포함하여 미래버전을 포함시킬지 여부")

    class Meta:
        managed = False
        db_table = 'curry_ad_balance'
        verbose_name = '광고 밸런스'
        verbose_name_plural = '광고 밸런스'


class CurryRdsScaleModifier(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(help_text="디비변경을 시작할 시간. 신규 생성은 20분가량, 삭제는 5분가량")
    number = models.IntegerField(help_text="1~5사이의 숫자. 30분이내에 2번이상 변경을 시도하지말것")
    description = models.CharField(max_length=255, blank=True, null=True, help_text="설명")
    status = models.CharField(max_length=9)
    ut = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'curry_rds_scale_modifier'
        verbose_name = 'RDS scale Modifier'
        verbose_name_plural = 'RDS scale Modifier'


class SwipsPush(models.Model):
    id = models.AutoField(primary_key=True)
    push_type = models.IntegerField()
    table_name = models.CharField(max_length=45)
    row_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=9)
    delayed_until = models.DateTimeField(blank=True, null=True)
    ref1 = models.IntegerField(blank=True, null=True)
    ref2 = models.IntegerField(blank=True, null=True)
    ref3 = models.IntegerField(blank=True, null=True)
    ref4 = models.IntegerField(blank=True, null=True)
    ref5 = models.IntegerField(blank=True, null=True)
    refstr1 = models.CharField(max_length=10, blank=True, null=True)
    refstr2 = models.CharField(max_length=2048, blank=True, null=True)
    refstr3 = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_push'
        verbose_name = 'Swips Push'
        verbose_name_plural = 'Swips Push'
