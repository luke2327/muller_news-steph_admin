# Generated by Django 2.0.4 on 2018-04-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurryPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name', models.CharField(blank=True, max_length=30, null=True)),
                ('name_ko', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name_ko', models.CharField(blank=True, max_length=30, null=True)),
                ('name_th', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name_th', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.IntegerField(blank=True, null=True)),
                ('social', models.CharField(blank=True, max_length=255, null=True)),
                ('draft', models.CharField(blank=True, max_length=30, null=True)),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('ut', models.DateTimeField()),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'curry_player',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SwipsLeagueInfo',
            fields=[
                ('league', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name', models.CharField(blank=True, max_length=30, null=True)),
                ('short_name', models.CharField(blank=True, max_length=6, null=True)),
                ('name_ko', models.CharField(blank=True, max_length=50, null=True)),
                ('name_pt', models.CharField(blank=True, max_length=50, null=True)),
                ('name_th', models.CharField(blank=True, max_length=50, null=True)),
                ('name_id', models.CharField(blank=True, max_length=50, null=True)),
                ('name_vi', models.CharField(blank=True, max_length=50, null=True)),
                ('no_teams', models.IntegerField(blank=True, null=True)),
                ('founded', models.IntegerField(blank=True, null=True)),
                ('last_champion', models.IntegerField(blank=True, null=True)),
                ('social', models.CharField(blank=True, max_length=255, null=True)),
                ('social_ko', models.CharField(blank=True, max_length=255, null=True)),
                ('social_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('social_id', models.CharField(blank=True, max_length=255, null=True)),
                ('social_th', models.CharField(blank=True, max_length=255, null=True)),
                ('social_vi', models.CharField(blank=True, max_length=255, null=True)),
                ('social_en', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=6, null=True)),
                ('category', models.IntegerField(blank=True, null=True)),
                ('host', models.CharField(blank=True, max_length=20, null=True)),
                ('ut', models.DateTimeField()),
            ],
            options={
                'db_table': 'swips_league_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SwipsPlayerInfo',
            fields=[
                ('player', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name', models.CharField(blank=True, max_length=30, null=True)),
                ('name_ko', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name_ko', models.CharField(blank=True, max_length=30, null=True)),
                ('name_th', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name_th', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.IntegerField(blank=True, null=True)),
                ('social', models.CharField(blank=True, max_length=255, null=True)),
                ('draft', models.CharField(blank=True, max_length=30, null=True)),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('ut', models.DateTimeField()),
            ],
            options={
                'db_table': 'swips_player_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SwipsTeamInfo',
            fields=[
                ('team', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name', models.CharField(blank=True, max_length=30, null=True)),
                ('short_name', models.CharField(blank=True, max_length=5, null=True)),
                ('name_ko', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name_ko', models.CharField(blank=True, max_length=30, null=True)),
                ('name_th', models.CharField(blank=True, max_length=50, null=True)),
                ('mid_name_th', models.CharField(blank=True, max_length=30, null=True)),
                ('color', models.CharField(blank=True, max_length=6, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('founded', models.IntegerField(blank=True, null=True)),
                ('last_rank', models.CharField(blank=True, max_length=30, null=True)),
                ('no_champions', models.IntegerField(blank=True, null=True)),
                ('manager', models.CharField(blank=True, max_length=50, null=True)),
                ('manager_ko', models.CharField(blank=True, max_length=50, null=True)),
                ('manager_th', models.CharField(blank=True, max_length=50, null=True)),
                ('social', models.CharField(blank=True, max_length=255, null=True)),
                ('social_ko', models.CharField(blank=True, max_length=255, null=True)),
                ('social_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('social_id', models.CharField(blank=True, max_length=255, null=True)),
                ('social_th', models.CharField(blank=True, max_length=255, null=True)),
                ('social_vi', models.CharField(blank=True, max_length=255, null=True)),
                ('ut', models.DateTimeField()),
            ],
            options={
                'db_table': 'swips_team_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SwipsPlayerCareer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('player', models.IntegerField(blank=True, null=True)),
                ('team', models.IntegerField(blank=True, null=True)),
                ('date_from', models.CharField(blank=True, max_length=12, null=True)),
                ('date_to', models.CharField(blank=True, max_length=12, null=True)),
                ('active', models.CharField(blank=True, max_length=5, null=True)),
                ('ut', models.CharField(blank=True, max_length=12, null=True)),
                ('on_loan', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
