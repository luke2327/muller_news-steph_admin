# Generated by Django 2.0.4 on 2018-05-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(blank=True, max_length=64, null=True)),
                ('pf', models.CharField(blank=True, max_length=8, null=True)),
                ('pf_user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('pf_user_name', models.CharField(blank=True, max_length=64, null=True)),
                ('pf_user_token', models.CharField(blank=True, max_length=2048, null=True)),
                ('pf_image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('email_confirmed', models.CharField(blank=True, max_length=3, null=True)),
                ('secret_key', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'verbose_name': '계정',
                'verbose_name_plural': '계정',
                'db_table': 'su_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuAccountFollowing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('type', models.CharField(max_length=2)),
                ('following', models.IntegerField()),
                ('push_type', models.IntegerField()),
                ('ut', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '계정 팔로잉',
                'verbose_name_plural': '계정 팔로잉',
                'db_table': 'su_account_following',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('account_id', models.IntegerField()),
                ('login_ut', models.DateTimeField(blank=True, null=True)),
                ('logout_ut', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '트랜젝션',
                'verbose_name_plural': '트랜젝션',
                'db_table': 'su_transaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('create_tmp', models.DateTimeField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=25, null=True)),
                ('os', models.CharField(blank=True, max_length=10, null=True)),
                ('push_key', models.CharField(blank=True, max_length=1023, null=True)),
                ('aws_endpoint', models.CharField(blank=True, max_length=255, null=True)),
                ('last_login_ut', models.DateTimeField(blank=True, null=True)),
                ('del_field', models.IntegerField(blank=True, db_column='del', null=True)),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'su_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuUserFollowing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('type', models.CharField(max_length=2)),
                ('following', models.IntegerField()),
                ('push_type', models.IntegerField()),
                ('language', models.CharField(max_length=5)),
                ('ut', models.DateTimeField()),
                ('aws_subscription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': '사용자 팔로잉',
                'verbose_name_plural': '사용자 팔로잉',
                'db_table': 'su_user_following',
                'managed': False,
            },
        ),
    ]