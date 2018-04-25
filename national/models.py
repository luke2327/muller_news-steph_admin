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
    team = models.AutoField(primary_key=True)
    competition = models.IntegerField()
    no_champions = models.IntegerField()
    appearance = models.IntegerField()
    best_result = models.CharField(max_length=20)
    no_champions_desc = models.CharField(max_length=15)
    appearance_desc = models.CharField(max_length=15)
    best_result_desc = models.CharField(max_length=15)
    last_result_desc = models.CharField(max_length=15)
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
