# Generated by Django 2.0.4 on 2018-05-10 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='swipslineupcustom',
            options={'managed': False, 'verbose_name': '라인업 수동입력', 'verbose_name_plural': '라인업 수동입력'},
        ),
        migrations.AlterModelOptions(
            name='swipsmatchdetailcustom',
            options={'managed': False, 'verbose_name': '매치팩트 수동입력', 'verbose_name_plural': '매치팩트 수동입력'},
        ),
    ]