from django.db import models
# from django_mysql.models import EnumField
# Create your models here.

class SwipsTransfer(models.Model):
    type_choice = (
        ('official', 'official'),
        ('agreed',  'agreed'),
        ('bid',  'bid'),
        ('rumor',  'rumor'),
    )
    contact_info_choice = (
        ('confirm','confirm'),
        ('estimate','estimate'),
        ('close','close'),
    )
    fee_info_choice = (
        ('confirm','confirm'),
        ('estimate','estimate'),
        ('close','close'),
    )
    fee_currency_coice = (
          ('euro','euro'),
          ('pound','pound'),
          ('dollar','dollar'),
          ('won','won'),
      )
    id = models.AutoField(primary_key=True)
    sport = models.IntegerField(help_text="1:football, 23: basketball, 26: baseball", default='1')
    player_id = models.IntegerField(help_text="swips_player id, 찾을 수 없을떄에는 1로 기록", default='0')
    player_name = models.CharField(max_length=45, blank=True, null=True, help_text="player_id를 찾을 수 없을때에만 영어로 기록")
    position = models.CharField(max_length=10, blank=True, null=True, help_text="항상 2자의 영어대문자로 기록")
    from_team_id = models.IntegerField(help_text="원 소속팀 id, 찾을 수 없을때에는 0으로 기록", default='0')
    from_team_name = models.CharField(max_length=45, blank=True, null=True, help_text="from_team_id를 찾을 수 없을때에만 영어로 기록(첫자 대문자!)")
    to_team_id = models.IntegerField(help_text="이적할 팀 id, 찾을 수 없을떄에는 0으로 기록", default='0')
    to_team_name = models.CharField(max_length=45, blank=True, null=True, help_text="to_team_id를 찾을 수 없을떄에만 영어로 기록(첫자 대문자!)")
    is_loan = models.IntegerField(help_text="0이면 이적, 1이면 임대", default='0')
    type = models.CharField(max_length=10, choices=type_choice, help_text="rumor:루머, bid:제안, agreed:확정, official:오피셜")
    ut = models.DateTimeField(blank=True, null=True)
    contract_dt = models.DateField(blank=True, null=True, help_text="신규계약 만료일", default='2000-01-01 00:00:00')
    contract_info = models.CharField(max_length=8, choices=contact_info_choice, help_text="close:contract_dt가 보이지 않게함, estimate: 추정, confirm: 확정")
    fee = models.BigIntegerField(help_text="이적금액 숫자로입력")
    fee_info = models.CharField(max_length=8, choices=fee_info_choice, help_text="close: fee가 보이지 않게함, estimate: 추정, confirm: 확정")
    fee_currency = models.CharField(max_length=6, choices=fee_currency_coice, help_text="통화")
    source_id = models.CharField(max_length=255, blank=True, null=True)
    source_th = models.CharField(max_length=255, blank=True, null=True)
    source_pt = models.CharField(max_length=255, blank=True, null=True)
    source_ko = models.CharField(max_length=255, blank=True, null=True)
    source_vi = models.CharField(max_length=255, blank=True, null=True)
    source_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_transfer'
        verbose_name = '이적'
        verbose_name_plural = '이적'
