from django.db import models

# Create your models here.

class SwipsNationalTeamInfoWC(models.Model):
    team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    fifa_ranking = models.PositiveIntegerField()
    no_champions = models.IntegerField()
    appearance = models.IntegerField()
    best_result = models.CharField(max_length=20)
    last_result = models.CharField(max_length=20)
    no_champions_desc = models.CharField(max_length=150)
    appearance_desc = models.CharField(max_length=150)
    best_result_desc = models.CharField(max_length=150)
    last_result_desc = models.CharField(max_length=150)


    class Meta:
        managed = False
        db_table = 'swips_national_team_info_wc'
        verbose_name = '국가별WC정보'
        verbose_name_plural = '국가별WC정보'
class SwipsNationalTeamInfoCompetition(models.Model):
    result_choice = (
        ('W','W'),
        ('F','F'),
        ('B','B'),
        ('4th','4th'),
        ('4','4'),
        ('8','8'),
        ('16','16'),
        ('32','32'),
        ('group stage','group stage'),
        ('qualification','qualification'),
        ('no info','no info'),
    )
    team = models.AutoField(primary_key=True)
    competition = models.IntegerField(help_text="[리그 id] 숫자로 입력")
    no_champions = models.IntegerField(help_text="우승횟수. 숫자로입력. 없으면 0, 정보가 없으면 -1")
    appearance = models.IntegerField(help_text="출전횟수. 숫자로 입력. 없으면 0, 정보가 없으면 -1")
    best_result = models.CharField(max_length=20, choices = result_choice, help_text='정보가 없으면 "no info"')
    last_result = models.CharField(max_length=20, choices = result_choice, help_text='정보가 없으면 "no info"')
    no_champions_desc = models.CharField(max_length=15)
    appearance_desc = models.CharField(max_length=15)
    best_result_desc = models.CharField(max_length=15)
    last_result_desc = models.CharField(max_length=15, help_text="괄호안에 최근결과 년도. 예) (2002)")
    valid_until = models.CharField(max_length=20)
    ut = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'swips_national_team_info_competition'
        verbose_name = '국가별대회정보'
        verbose_name_plural = '국가별대회정보'
class SwipsNationalCompetitionInfo(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    name_ko = models.CharField(max_length=50)
    name_pt = models.CharField(max_length=50)
    name_th = models.CharField(max_length=50)
    name_id = models.CharField(max_length=50)
    name_vi = models.CharField(max_length=50)
    ut = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'swips_national_competition_info'
        verbose_name = '대회이름입력'
        verbose_name_plural = '대회이름입력'
