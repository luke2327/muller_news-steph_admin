# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from steph.static.py.choices import *


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bettingoffer(models.Model):
    outcomefk = models.PositiveIntegerField(db_column='outcomeFK')  # Field name made lowercase.
    odds_providerfk = models.PositiveIntegerField(db_column='odds_providerFK')  # Field name made lowercase.
    odds = models.FloatField()
    odds_old = models.FloatField()
    active = models.CharField(max_length=3)
    is_back = models.CharField(max_length=3)
    is_single = models.CharField(max_length=3)
    is_live = models.CharField(max_length=3)
    volume = models.IntegerField()
    currency = models.CharField(max_length=4)
    couponkey = models.CharField(db_column='couponKey', max_length=255)  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bettingoffer'


class Country(models.Model):
    name = models.CharField(max_length=50)
    enetid = models.PositiveIntegerField(db_column='enetID')  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    name_id = models.CharField(max_length=50, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    name_vi = models.CharField(max_length=50, blank=True, null=True)
    name_pt = models.CharField(max_length=50, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class CurryAdBalance(models.Model):
    type = models.CharField(max_length=8)
    weight = models.IntegerField()
    country_cd = models.CharField(max_length=2)
    os = models.CharField(max_length=7)
    valid_until = models.DateTimeField(blank=True, null=True)
    ut = models.DateTimeField()
    advertiser = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    ad_type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'curry_ad_balance'


class CurryExposePostLog(models.Model):
    target = models.ForeignKey('CurryExposeTarget', models.DO_NOTHING, db_column='target')
    user = models.CharField(max_length=45)
    desc = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'curry_expose_post_log'


class CurryExposeTarget(models.Model):
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'curry_expose_target'


class CurryFollowingCount(models.Model):
    following = models.IntegerField()
    count = models.BigIntegerField()
    type = models.CharField(max_length=2)
    league = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    teams_league = models.CharField(max_length=50, blank=True, null=True)
    player = models.CharField(max_length=50, blank=True, null=True)
    players_team = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_following_count'


class CurryInfoDbModify(models.Model):
    item = models.IntegerField()
    type = models.CharField(max_length=2)
    migrate_item = models.IntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    valid_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_info_db_modify'


class CurryInfoImageModify(models.Model):
    item = models.IntegerField()
    type = models.CharField(max_length=2)
    desc = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    valid_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_info_image_modify'


class CurryPlayer(models.Model):
    player = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    mid_name_ko = models.CharField(max_length=30, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    mid_name_th = models.CharField(max_length=30, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    draft = models.CharField(max_length=30, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    ut = models.DateTimeField()
    position = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_player'


class CurryRdsScaleModifier(models.Model):
    time = models.DateTimeField()
    number = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=9)
    ut = models.DateTimeField()
    user = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'curry_rds_scale_modifier'


class CustomListManagerLineupNationalTeam(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    manager_name = models.CharField(max_length=50, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_list_manager_lineup_national_team'


class CustomListManagerLineupTeam(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    manager_name = models.CharField(max_length=50, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_list_manager_lineup_team'


class CustomListManagerNt(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    manager_name = models.CharField(max_length=50, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_list_manager_nt'


class CustomListManagerT(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    manager_name = models.CharField(max_length=50, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_list_manager_t'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class Draw(models.Model):
    name = models.CharField(max_length=255)
    object_typefk = models.IntegerField(db_column='object_typeFK')  # Field name made lowercase.
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    draw_typefk = models.IntegerField(db_column='draw_typeFK')  # Field name made lowercase.
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'draw'


class DrawConfig(models.Model):
    name = models.CharField(max_length=255)
    drawfk = models.IntegerField(db_column='drawFK')  # Field name made lowercase.
    value = models.CharField(max_length=255)
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'draw_config'


class DrawDetail(models.Model):
    drawfk = models.IntegerField(db_column='drawFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    rank = models.CharField(max_length=5)
    value = models.CharField(max_length=5)
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'draw_detail'


class DrawEvent(models.Model):
    name = models.CharField(max_length=255)
    drawfk = models.IntegerField(db_column='drawFK')  # Field name made lowercase.
    round_typefk = models.IntegerField(db_column='round_typeFK')  # Field name made lowercase.
    draw_eventfk = models.IntegerField(db_column='draw_eventFK')  # Field name made lowercase.
    draw_order = models.IntegerField()
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'draw_event'


class DrawEventDetail(models.Model):
    draw_eventfk = models.IntegerField(db_column='draw_eventFK')  # Field name made lowercase.
    object_typefk = models.IntegerField(db_column='object_typeFK')  # Field name made lowercase.
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    startdate = models.DateTimeField(blank=True, null=True)
    rank = models.IntegerField()
    draw_event_detailfk = models.IntegerField(db_column='draw_event_detailFK')  # Field name made lowercase.
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'draw_event_detail'


class DrawEventParticipants(models.Model):
    draw_eventfk = models.IntegerField(db_column='draw_eventFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    number = models.IntegerField()
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'draw_event_participants'


class DrawType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'draw_type'


class Event(models.Model):
    name = models.CharField(max_length=150)
    tournament_stagefk = models.PositiveIntegerField(db_column='tournament_stageFK')  # Field name made lowercase.
    startdate = models.DateTimeField(blank=True, null=True)
    eventstatusfk = models.PositiveIntegerField(db_column='eventstatusFK')  # Field name made lowercase.
    status_type = models.CharField(max_length=11)
    status_descfk = models.PositiveIntegerField(db_column='status_descFK')  # Field name made lowercase.
    enetid = models.IntegerField(db_column='enetID')  # Field name made lowercase.
    enetsportid = models.CharField(db_column='enetSportID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    locked = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'event'


class EventIncident(models.Model):
    eventfk = models.PositiveIntegerField(db_column='eventFK')  # Field name made lowercase.
    sportfk = models.PositiveIntegerField(db_column='sportFK')  # Field name made lowercase.
    event_incident_typefk = models.PositiveIntegerField(db_column='event_incident_typeFK')  # Field name made lowercase.
    enetid = models.IntegerField(db_column='enetID', blank=True, null=True)  # Field name made lowercase.
    elapsed = models.IntegerField()
    elapsed_plus = models.IntegerField()
    comment = models.CharField(max_length=50)
    sortorder = models.IntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_incident'


class EventIncidentDetail(models.Model):
    type = models.CharField(max_length=16)
    event_incidentfk = models.PositiveIntegerField(db_column='event_incidentFK')  # Field name made lowercase.
    participantfk = models.PositiveIntegerField(db_column='participantFK')  # Field name made lowercase.
    value = models.CharField(max_length=255)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_incident_detail'


class EventIncidentType(models.Model):
    player1 = models.CharField(max_length=3)
    player2 = models.CharField(max_length=3)
    team = models.CharField(max_length=3)
    comment = models.CharField(max_length=50)
    subtype1 = models.CharField(max_length=50)
    subtype2 = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    enetid = models.IntegerField(db_column='enetID', blank=True, null=True)  # Field name made lowercase.
    comment_type = models.CharField(max_length=50)
    player2_type = models.CharField(max_length=50)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_incident_type'
        unique_together = (('player1', 'player2', 'team', 'comment', 'subtype1', 'subtype2', 'type', 'del_field'),)


class EventIncidentTypeText(models.Model):
    event_incident_typefk = models.PositiveIntegerField(db_column='event_incident_typeFK')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    enetid = models.PositiveIntegerField(db_column='enetID')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_incident_type_text'


class EventParticipants(models.Model):
    number = models.PositiveIntegerField()
    participantfk = models.PositiveIntegerField(db_column='participantFK')  # Field name made lowercase.
    eventfk = models.PositiveIntegerField(db_column='eventFK')  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'event_participants'


class EventScope(models.Model):
    eventfk = models.IntegerField(db_column='eventFK')  # Field name made lowercase.
    scope_typefk = models.IntegerField(db_column='scope_typeFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_scope'


class EventScopeDetail(models.Model):
    event_scopefk = models.IntegerField(db_column='event_scopeFK')  # Field name made lowercase.
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_scope_detail'


class GreenTopic(models.Model):
    topic_arn = models.CharField(unique=True, max_length=255, blank=True, null=True)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'green_topic'


class Image(models.Model):
    object = models.CharField(max_length=22)
    objectfk = models.PositiveIntegerField(db_column='objectFK')  # Field name made lowercase.
    type = models.CharField(max_length=7)
    contenttype = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    value = models.TextField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'image'


class Incident(models.Model):
    event_participantsfk = models.PositiveIntegerField(db_column='event_participantsFK')  # Field name made lowercase.
    incident_typefk = models.PositiveIntegerField(db_column='incident_typeFK')  # Field name made lowercase.
    incident_code = models.CharField(max_length=9)
    enetid = models.IntegerField(db_column='enetID', blank=True, null=True)  # Field name made lowercase.
    enetsportid = models.CharField(db_column='enetSportID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    elapsed = models.IntegerField()
    sortorder = models.IntegerField()
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ref_participantfk = models.PositiveIntegerField(db_column='ref_participantFK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incident'


class IncidentType(models.Model):
    name = models.CharField(max_length=50)
    subtype = models.CharField(max_length=8)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'incident_type'


class Language(models.Model):
    object = models.CharField(max_length=24, blank=True, null=True)
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    language_typefk = models.IntegerField(db_column='language_typeFK')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    locked = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'language'


class LanguageType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'language_type'


class Lineup(models.Model):
    event_participantsfk = models.PositiveIntegerField(db_column='event_participantsFK')  # Field name made lowercase.
    participantfk = models.PositiveIntegerField(db_column='participantFK')  # Field name made lowercase.
    lineup_typefk = models.PositiveIntegerField(db_column='lineup_typeFK')  # Field name made lowercase.
    shirt_number = models.PositiveIntegerField()
    pos = models.IntegerField()
    enet_pos = models.PositiveIntegerField()
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'lineup'


class LineupScopeResult(models.Model):
    lineupfk = models.IntegerField(db_column='lineupFK')  # Field name made lowercase.
    event_scopefk = models.IntegerField(db_column='event_scopeFK')  # Field name made lowercase.
    scope_data_typefk = models.IntegerField(db_column='scope_data_typeFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineup_scope_result'


class LineupType(models.Model):
    name = models.CharField(max_length=50)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'lineup_type'


class LiveoddsBettingoffer(models.Model):
    object = models.CharField(max_length=19)
    objectfk = models.PositiveIntegerField(db_column='objectFK')  # Field name made lowercase.
    odds_providerfk = models.PositiveIntegerField(db_column='odds_providerFK')  # Field name made lowercase.
    liveodds_typefk = models.IntegerField(db_column='liveodds_typeFK')  # Field name made lowercase.
    liveodds_subtypefk = models.PositiveIntegerField(db_column='liveodds_subtypeFK')  # Field name made lowercase.
    liveodds_scopefk = models.IntegerField(db_column='liveodds_scopeFK')  # Field name made lowercase.
    liveodds_statusfk = models.PositiveIntegerField(db_column='liveodds_statusFK')  # Field name made lowercase.
    iparam1 = models.IntegerField()
    iparam2 = models.IntegerField()
    dparam1 = models.FloatField()
    dparam2 = models.FloatField()
    sparam = models.CharField(max_length=20)
    value = models.FloatField()
    value_old = models.FloatField()
    n = models.PositiveIntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'liveodds_bettingoffer'


class LiveoddsBettingofferAverage(models.Model):
    object = models.CharField(max_length=19)
    objectfk = models.PositiveIntegerField(db_column='objectFK')  # Field name made lowercase.
    liveodds_typefk = models.IntegerField(db_column='liveodds_typeFK')  # Field name made lowercase.
    liveodds_subtypefk = models.PositiveIntegerField(db_column='liveodds_subtypeFK')  # Field name made lowercase.
    liveodds_scopefk = models.IntegerField(db_column='liveodds_scopeFK')  # Field name made lowercase.
    liveodds_statusfk = models.IntegerField(db_column='liveodds_statusFK')  # Field name made lowercase.
    iparam1 = models.IntegerField()
    iparam2 = models.IntegerField()
    dparam1 = models.FloatField()
    dparam2 = models.FloatField()
    sparam = models.CharField(max_length=20)
    value = models.FloatField()
    value_old = models.FloatField()
    n = models.PositiveIntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'liveodds_bettingoffer_average'


class LiveoddsScope(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    n = models.PositiveIntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'liveodds_scope'


class LiveoddsStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    n = models.PositiveIntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'liveodds_status'


class LiveoddsSubtype(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    n = models.PositiveIntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'liveodds_subtype'


class LiveoddsType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    n = models.PositiveIntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'liveodds_type'


class ObjectParticipants(models.Model):
    object = models.CharField(max_length=19, blank=True, null=True)
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    participantfk = models.PositiveIntegerField(db_column='participantFK')  # Field name made lowercase.
    participant_type = models.CharField(max_length=9)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=3)
    enetid = models.PositiveIntegerField(db_column='enetID')  # Field name made lowercase.
    enetsportid = models.CharField(db_column='enetSportID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_participants'


class ObjectType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'object_type'


class OddsProvider(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    countryfk = models.PositiveIntegerField(db_column='countryFK')  # Field name made lowercase.
    bookmaker = models.CharField(max_length=3)
    preferred = models.CharField(max_length=3)
    betex = models.CharField(max_length=3)
    active = models.CharField(max_length=3)
    n = models.PositiveIntegerField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'odds_provider'


class OffenceType(models.Model):
    name = models.CharField(max_length=50)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'offence_type'


class Outcome(models.Model):
    object = models.CharField(max_length=19)
    objectfk = models.PositiveIntegerField(db_column='objectFK')  # Field name made lowercase.
    type = models.CharField(max_length=6)
    event_participant_number = models.IntegerField()
    scope = models.CharField(max_length=3)
    subtype = models.CharField(max_length=8)
    iparam = models.IntegerField()
    iparam2 = models.IntegerField()
    dparam = models.FloatField()
    dparam2 = models.FloatField()
    sparam = models.CharField(max_length=20)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'outcome'


class Participant(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=9)
    type = models.CharField(max_length=12)
    countryfk = models.PositiveIntegerField(db_column='countryFK')  # Field name made lowercase.
    enetid = models.PositiveIntegerField(db_column='enetID')  # Field name made lowercase.
    enetsportid = models.CharField(db_column='enetSportID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'participant'


class Property(models.Model):
    object = models.CharField(max_length=22)
    objectfk = models.PositiveIntegerField(db_column='objectFK')  # Field name made lowercase.
    type = models.CharField(max_length=17)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255, blank=True, null=True)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'property'


class Reference(models.Model):
    object = models.CharField(max_length=19)
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    refers_to = models.IntegerField()
    name = models.CharField(max_length=255)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    reference_typefk = models.IntegerField(db_column='reference_typeFK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reference'


class ReferenceType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_type'


class Result(models.Model):
    event_participantsfk = models.PositiveIntegerField(db_column='event_participantsFK')  # Field name made lowercase.
    result_typefk = models.PositiveIntegerField(db_column='result_typeFK')  # Field name made lowercase.
    result_code = models.CharField(max_length=16)
    value = models.CharField(max_length=255)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'result'


class ResultType(models.Model):
    name = models.CharField(max_length=50)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'result_type'


class RoundType(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    knockout = models.CharField(max_length=3)
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'round_type'


class SavedXml(models.Model):
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saved_xml'


class ScopeDataType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scope_data_type'


class ScopeResult(models.Model):
    event_participantsfk = models.IntegerField(db_column='event_participantsFK')  # Field name made lowercase.
    event_scopefk = models.IntegerField(db_column='event_scopeFK')  # Field name made lowercase.
    scope_data_typefk = models.IntegerField(db_column='scope_data_typeFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scope_result'


class ScopeType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scope_type'


class Sport(models.Model):
    name = models.CharField(max_length=50)
    enetsportcode = models.CharField(db_column='enetSportCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'sport'


class Standing(models.Model):
    object = models.CharField(max_length=19)
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    standing_typefk = models.IntegerField(db_column='standing_typeFK')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standing'


class StandingConfig(models.Model):
    standingfk = models.IntegerField(db_column='standingFK')  # Field name made lowercase.
    standing_type_paramfk = models.IntegerField(db_column='standing_type_paramFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    value = models.CharField(max_length=255)
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    sub_param = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'standing_config'
        unique_together = (('id', 'standingfk', 'standing_type_paramfk'),)


class StandingData(models.Model):
    standing_participantsfk = models.IntegerField(db_column='standing_participantsFK')  # Field name made lowercase.
    standing_type_paramfk = models.IntegerField(db_column='standing_type_paramFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    sub_param = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'standing_data'


class StandingParticipants(models.Model):
    standingfk = models.IntegerField(db_column='standingFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    rank = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'standing_participants'


class StandingType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standing_type'


class StandingTypeParam(models.Model):
    standing_typefk = models.IntegerField(db_column='standing_typeFK')  # Field name made lowercase.
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=9)
    value = models.CharField(max_length=255)
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standing_type_param'


class StatRules(models.Model):
    rule = models.CharField(max_length=255)
    rule_type = models.CharField(max_length=11)
    object_type = models.CharField(max_length=6)
    homeaway = models.CharField(max_length=3)
    matchrange = models.CharField(max_length=20)
    h2h = models.CharField(max_length=3)
    sub_param = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=8)
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'stat_rules'


class Statistic(models.Model):
    object_typefk = models.IntegerField(db_column='object_typeFK')  # Field name made lowercase.
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    statistic_typefk = models.IntegerField(db_column='statistic_typeFK')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic'


class StatisticConfig(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_config'
        unique_together = (('id', 'statisticfk', 'statistic_data_typefk'),)


class StatisticData1(models.Model):
    statistic_participants1fk = models.IntegerField(db_column='statistic_participants1FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data1'


class StatisticData2(models.Model):
    statistic_participants2fk = models.IntegerField(db_column='statistic_participants2FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data2'


class StatisticData3(models.Model):
    statistic_participants3fk = models.IntegerField(db_column='statistic_participants3FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data3'


class StatisticData4(models.Model):
    statistic_participants4fk = models.IntegerField(db_column='statistic_participants4FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data4'


class StatisticData5(models.Model):
    statistic_participants5fk = models.IntegerField(db_column='statistic_participants5FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data5'


class StatisticData6(models.Model):
    statistic_participants6fk = models.IntegerField(db_column='statistic_participants6FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data6'


class StatisticData7(models.Model):
    statistic_participants7fk = models.IntegerField(db_column='statistic_participants7FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data7'


class StatisticData8(models.Model):
    statistic_participants8fk = models.IntegerField(db_column='statistic_participants8FK')  # Field name made lowercase.
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    statistic_data_type_detailfk = models.IntegerField(db_column='statistic_data_type_detailFK')  # Field name made lowercase.
    value = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data8'


class StatisticDataType(models.Model):
    name = models.CharField(max_length=255)
    statistic_typefk = models.IntegerField(db_column='statistic_typeFK')  # Field name made lowercase.
    statistic_data_type_categoryfk = models.IntegerField(db_column='statistic_data_type_categoryFK')  # Field name made lowercase.
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data_type'


class StatisticDataTypeCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data_type_category'


class StatisticDataTypeDetail(models.Model):
    statistic_data_typefk = models.IntegerField(db_column='statistic_data_typeFK')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_data_type_detail'


class StatisticParticipants1(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants1'


class StatisticParticipants2(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants2'


class StatisticParticipants3(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants3'


class StatisticParticipants4(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants4'


class StatisticParticipants5(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants5'


class StatisticParticipants6(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants6'


class StatisticParticipants7(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants7'


class StatisticParticipants8(models.Model):
    statisticfk = models.IntegerField(db_column='statisticFK')  # Field name made lowercase.
    participantfk = models.IntegerField(db_column='participantFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_participants8'


class StatisticType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistic_type'


class StatsLive(models.Model):
    stat_rulesfk = models.IntegerField(db_column='stat_rulesFK')  # Field name made lowercase.
    participantfk = models.PositiveIntegerField(db_column='participantFK')  # Field name made lowercase.
    eventfk = models.PositiveIntegerField(db_column='eventFK')  # Field name made lowercase.
    teamfk = models.PositiveIntegerField(db_column='teamFK')  # Field name made lowercase.
    trigger_type = models.CharField(max_length=255)
    matchcount = models.PositiveIntegerField()
    value = models.CharField(max_length=255)
    value_div_matchcount = models.FloatField()
    incidentfk = models.IntegerField(db_column='incidentFK')  # Field name made lowercase.
    outcomefk = models.IntegerField(db_column='outcomeFK')  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'stats_live'


class StatsOdds(models.Model):
    stat_rulesfk = models.IntegerField(db_column='stat_rulesFK')  # Field name made lowercase.
    param = models.CharField(max_length=20)
    name = models.TextField()
    type = models.CharField(max_length=50)
    n = models.IntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'stats_odds'


class StatusDesc(models.Model):
    name = models.CharField(max_length=50)
    enetstatusid = models.PositiveIntegerField(db_column='enetStatusID')  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField()
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    status_type = models.CharField(max_length=11)
    mapto = models.IntegerField(db_column='mapTo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status_desc'


class SuAccount(models.Model):
    id = models.IntegerField(primary_key=True)
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


class SuAccountFollowing(models.Model):
    account_id = models.IntegerField()
    type = models.CharField(max_length=2)
    following = models.IntegerField()
    push_type = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'su_account_following'
        unique_together = (('account_id', 'type', 'following', 'push_type'),)


class SuTransaction(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    account_id = models.IntegerField()
    login_ut = models.DateTimeField(blank=True, null=True)
    logout_ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'su_transaction'
        unique_together = (('user_id', 'account_id', 'login_ut'),)


class SuUser(models.Model):
    id = models.IntegerField(primary_key=True)
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


class SuUserFollowing(models.Model):
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


class SwipsBoard(models.Model):
    item = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=2)
    participant = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=2)
    text = models.TextField(blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_board'


class SwipsBoardLike(models.Model):
    type = models.CharField(max_length=2)
    root_id = models.IntegerField()
    account_id = models.IntegerField()
    account_type = models.CharField(max_length=5)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_board_like'
        unique_together = (('type', 'root_id', 'account_id'),)


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
        db_table = 'swips_board_post'


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
        db_table = 'swips_board_reply'


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


class SwipsClientVersion(models.Model):
    timestamp = models.DateTimeField()
    link = models.CharField(max_length=200, blank=True, null=True)
    desription = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_client_version'


class SwipsCrawlingSource(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    source = models.CharField(max_length=45)
    content_type = models.CharField(max_length=4)
    sport = models.IntegerField()
    language_cd = models.CharField(max_length=2)
    frequency_cl = models.IntegerField(choices=IMPORTANCE_CHOICES, default=1)
    importance_cl = models.IntegerField(choices=IMPORTANCE_CHOICES, default=1)
    ut = models.CharField(max_length=10)
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'swips_crawling_source'
        unique_together = (('source', 'content_type', 'sport', 'language_cd'),)
        verbose_name = '크롤링 소스 리스트'
        verbose_name_plural = '크롤링 소스 리스트'


class SwipsFeedback(models.Model):
    user_id = models.IntegerField()
    user_agent = models.CharField(max_length=255)
    language = models.CharField(max_length=10, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    email = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_feedback'


class SwipsFixtures(models.Model):
    elapsed = models.IntegerField(blank=True, null=True)
    elapsed_plus = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    status = models.PositiveIntegerField()
    tournament_stage = models.PositiveIntegerField()
    tournament = models.PositiveIntegerField(blank=True, null=True)
    league = models.IntegerField()
    startdate = models.DateTimeField(blank=True, null=True)
    status_type = models.CharField(max_length=11)
    team1 = models.PositiveIntegerField(blank=True, null=True)
    team2 = models.PositiveIntegerField(blank=True, null=True)
    event_team1 = models.IntegerField(blank=True, null=True)
    event_team2 = models.IntegerField(blank=True, null=True)
    team1_score = models.PositiveIntegerField()
    team2_score = models.PositiveIntegerField()
    team1_score_extra = models.PositiveIntegerField()
    team2_score_extra = models.PositiveIntegerField()
    team1_score_so = models.PositiveIntegerField()
    team2_score_so = models.PositiveIntegerField()
    round = models.CharField(max_length=45, blank=True, null=True)
    stadium = models.CharField(max_length=255, blank=True, null=True)
    referee = models.BigIntegerField()
    gamestarted = models.DateTimeField(blank=True, null=True)
    firsthalfended = models.DateTimeField(blank=True, null=True)
    secondhalfstarted = models.DateTimeField(blank=True, null=True)
    spectators = models.CharField(max_length=255, blank=True, null=True)
    gameended = models.DateTimeField(blank=True, null=True)
    secondhalfended = models.DateTimeField(blank=True, null=True)
    exstarted = models.DateTimeField(blank=True, null=True)
    ex2ended = models.DateTimeField(blank=True, null=True)
    elapsedtime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'swips_fixtures'


class SwipsFixturesInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    broadcast_id = models.CharField(max_length=50, blank=True, null=True)
    broadcast_th = models.CharField(max_length=50, blank=True, null=True)
    broadcast_vn = models.CharField(max_length=50, blank=True, null=True)
    broadcast_br = models.CharField(max_length=50, blank=True, null=True)
    broadcast_kr = models.CharField(max_length=50, blank=True, null=True)
    broadcast_ph = models.CharField(max_length=50, blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_fixtures_info'


class SwipsInjury(models.Model):
    player = models.IntegerField(primary_key=True)
    injury = models.CharField(max_length=20, blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    return_str = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_injury'


class SwipsLeague(models.Model):
    id = models.IntegerField(primary_key=True)
    ut = models.DateTimeField(blank=True, null=True)
    season = models.CharField(max_length=50, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    sport = models.PositiveIntegerField(blank=True, null=True)
    group_concat_ts_name_separator_field = models.TextField(db_column="GROUP_CONCAT(ts.name SEPARATOR ',')", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_league'


class SwipsLeagueInfo(models.Model):
    league = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    short_name = models.CharField(max_length=6, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    name_pt = models.CharField(max_length=50, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    name_id = models.CharField(max_length=50, blank=True, null=True)
    name_vi = models.CharField(max_length=50, blank=True, null=True)
    no_teams = models.IntegerField(blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)
    last_champion = models.IntegerField(blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    social_ko = models.CharField(max_length=255, blank=True, null=True)
    social_pt = models.CharField(max_length=255, blank=True, null=True)
    social_id = models.CharField(max_length=255, blank=True, null=True)
    social_th = models.CharField(max_length=255, blank=True, null=True)
    social_vi = models.CharField(max_length=255, blank=True, null=True)
    social_en = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=6, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=20, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_league_info'


class SwipsLineupCustom(models.Model):
    match_id = models.IntegerField()
    team = models.IntegerField()
    lineup_number = models.IntegerField(blank=True, null=True)
    shirt_number = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=45)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_lineup_custom'
        unique_together = (('match_id', 'team', 'lineup_number'),)


class SwipsLog(models.Model):
    ref1 = models.IntegerField(blank=True, null=True)
    ref2 = models.IntegerField(blank=True, null=True)
    ref3 = models.IntegerField(blank=True, null=True)
    refstr1 = models.CharField(max_length=255, blank=True, null=True)
    refstr2 = models.CharField(max_length=255, blank=True, null=True)
    refstr3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_log'


class SwipsMatchDetailCustom(models.Model):
    match_id = models.IntegerField()
    team_id = models.IntegerField()
    lineup_number = models.IntegerField(blank=True, null=True)
    shirt_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=45)
    type = models.IntegerField()
    minute = models.IntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_match_detail_custom'
        unique_together = (('match_id', 'team_id', 'name', 'type', 'minute'),)


class SwipsMatchStat(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    ut = models.DateTimeField(blank=True, null=True)
    player = models.PositiveIntegerField()
    team = models.PositiveIntegerField(blank=True, null=True)
    event_participant = models.PositiveIntegerField()
    match = models.IntegerField(blank=True, null=True)
    status_type = models.CharField(max_length=11, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    data_type = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    lineup_type = models.PositiveIntegerField()
    shirt_number = models.PositiveIntegerField()
    pos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'swips_match_stat'


class SwipsNationalTeamInfo(models.Model):
    team = models.IntegerField(primary_key=True)
    fifa_ranking = models.IntegerField()
    wc_no_champions = models.IntegerField()
    wc_appearance = models.IntegerField()
    wc_best_result = models.CharField(max_length=13)
    wc_last_result = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'swips_national_team_info'


class SwipsNews(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    language_cd = models.CharField(max_length=2, blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    is_top = models.IntegerField()
    sport = models.IntegerField(blank=True, null=True)
    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    is_frifee_content = models.IntegerField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    following_desc = models.CharField(max_length=255, blank=True, null=True)
    pushed = models.IntegerField()
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'swips_news'

class CurryNews(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    language_cd = models.CharField(max_length=2, blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    is_top = models.IntegerField()
    sport = models.IntegerField(blank=True, null=True)
    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    is_frifee_content = models.IntegerField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    following_desc = models.CharField(max_length=255, blank=True, null=True)
    pushed = models.IntegerField()
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    pl_relation = models.CharField(max_length=255, blank=True, null=True)
    te_relation = models.CharField(max_length=255, blank=True, null=True)
    le_relation = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'curry_news'
        verbose_name = "뉴스"
        verbose_name_plural = "뉴스"
class SwipsNewsRelation(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    participant = models.IntegerField()
    news_id = models.IntegerField()
    tmp = models.DateTimeField()
    type = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'swips_news_relation'
        unique_together = (('participant', 'news_id'),)


class SwipsNotification(models.Model):
    ut_from = models.DateTimeField()
    ut_to = models.DateTimeField()
    title = models.CharField(max_length=50, blank=True, null=True)
    title_th = models.CharField(max_length=50, blank=True, null=True)
    title_pt = models.CharField(max_length=50, blank=True, null=True)
    title_ko = models.CharField(max_length=50, blank=True, null=True)
    title_id = models.CharField(max_length=50, blank=True, null=True)
    title_vi = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    message_th = models.TextField(blank=True, null=True)
    message_pt = models.TextField(blank=True, null=True)
    message_ko = models.TextField(blank=True, null=True)
    message_id = models.TextField(blank=True, null=True)
    message_vi = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=18)
    client_version = models.IntegerField()
    platform = models.CharField(max_length=3, blank=True, null=True)
    include_lower_versions = models.CharField(max_length=3, blank=True, null=True)
    active = models.CharField(max_length=3, blank=True, null=True)
    include_upper_versions = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_notification'


class SwipsPlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    ut = models.DateTimeField(blank=True, null=True)
    ut2 = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50)
    country = models.PositiveIntegerField()
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    shirt_number = models.CharField(max_length=255, blank=True, null=True)
    on_loan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_player'


class SwipsPlayerInfo(models.Model):
    player = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    mid_name_ko = models.CharField(max_length=30, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    mid_name_th = models.CharField(max_length=30, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    draft = models.CharField(max_length=30, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_player_info'


class SwipsPlayerNational(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.PositiveIntegerField()
    position = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    national_team = models.IntegerField()
    team = models.IntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=50, blank=True, null=True)
    shirt_number = models.CharField(max_length=255, blank=True, null=True)
    on_loan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_player_national'


class SwipsPoll(models.Model):
    item = models.IntegerField()
    number = models.IntegerField()
    type = models.CharField(max_length=2, blank=True, null=True)
    participant = models.IntegerField(blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_poll'
        unique_together = (('type', 'participant', 'item'),)


class SwipsPush(models.Model):
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


class SwipsQna(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    account_id = models.IntegerField()
    user_agent = models.CharField(max_length=255)
    language = models.CharField(max_length=32, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    img_ext = models.CharField(max_length=5, blank=True, null=True)
    img_rot = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    answer_ut = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    field_del = models.IntegerField(db_column='_del')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'swips_qna'


class SwipsRating(models.Model):
    match_id = models.IntegerField()
    player_id = models.IntegerField()
    type = models.IntegerField()
    rating = models.FloatField()
    source = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'swips_rating'
        unique_together = (('match_id', 'player_id', 'source'),)


class SwipsRatingProperty(models.Model):
    id = models.IntegerField(primary_key=True)
    mom_id = models.IntegerField(blank=True, null=True)
    mom_goal = models.IntegerField(blank=True, null=True)
    mom_assist = models.IntegerField(blank=True, null=True)
    mom_min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_rating_property'


class SwipsRedis(models.Model):
    type = models.CharField(max_length=7)
    flw_id = models.IntegerField(blank=True, null=True)
    flw_type = models.CharField(max_length=2)
    language_cd = models.CharField(max_length=2, blank=True, null=True)
    dml_type = models.CharField(max_length=8)
    content_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=9)
    ut = models.DateTimeField()
    ct = models.DateTimeField()
    status_ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_redis'


class SwipsReview(models.Model):
    id = models.IntegerField(primary_key=True)
    sport = models.IntegerField()
    league = models.IntegerField()
    result = models.TextField(blank=True, null=True)
    ut = models.DateTimeField()
    standing = models.TextField(blank=True, null=True)
    startdate = models.DateTimeField()
    ct = models.DateTimeField()
    pushed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'swips_review'


class SwipsShortclip(models.Model):
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    is_top = models.IntegerField(blank=True, null=True)
    sport = models.IntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_shortclip'


class SwipsShortclipRelation(models.Model):
    participant = models.IntegerField(primary_key=True)
    shortclip_id = models.IntegerField()
    tmp = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_shortclip_relation'
        unique_together = (('participant', 'shortclip_id'),)


class SwipsStandingLiveTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.IntegerField()
    rank = models.PositiveIntegerField()
    tournament = models.PositiveIntegerField(blank=True, null=True)
    league = models.IntegerField()
    tournament_stage = models.IntegerField(blank=True, null=True)
    standingfk = models.IntegerField(db_column='standingFK')  # Field name made lowercase.
    played = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    wins = models.BigIntegerField(blank=True, null=True)
    draws = models.BigIntegerField(blank=True, null=True)
    defeits = models.BigIntegerField(blank=True, null=True)
    goalsfor = models.BigIntegerField(blank=True, null=True)
    goalsagainst = models.BigIntegerField(blank=True, null=True)
    div = models.CharField(max_length=255)
    conf = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_standing_live_team'


class SwipsStandingPlayer23(models.Model):
    player = models.PositiveIntegerField(primary_key=True)
    team = models.IntegerField()
    league = models.IntegerField()
    gp = models.BigIntegerField(db_column='GP')  # Field name made lowercase.
    pts = models.DecimalField(db_column='PTS', max_digits=65, decimal_places=0)  # Field name made lowercase.
    ppg = models.DecimalField(db_column='PPG', max_digits=65, decimal_places=4)  # Field name made lowercase.
    fga = models.DecimalField(db_column='FGA', max_digits=65, decimal_places=0)  # Field name made lowercase.
    fg = models.DecimalField(db_column='FG', max_digits=65, decimal_places=0)  # Field name made lowercase.
    fgpct = models.DecimalField(db_column='FGPCT', max_digits=65, decimal_places=4)  # Field name made lowercase.
    number_3p = models.DecimalField(db_column='3P', max_digits=65, decimal_places=0)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3pa = models.DecimalField(db_column='3PA', max_digits=65, decimal_places=0)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ppct = models.DecimalField(db_column='3PPCT', max_digits=65, decimal_places=4)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ft = models.DecimalField(db_column='FT', max_digits=65, decimal_places=0)  # Field name made lowercase.
    fta = models.DecimalField(db_column='FTA', max_digits=65, decimal_places=0)  # Field name made lowercase.
    ftpct = models.DecimalField(db_column='FTPCT', max_digits=65, decimal_places=4)  # Field name made lowercase.
    ast = models.DecimalField(db_column='AST', max_digits=65, decimal_places=0)  # Field name made lowercase.
    apg = models.DecimalField(db_column='APG', max_digits=65, decimal_places=4)  # Field name made lowercase.
    pf = models.DecimalField(db_column='PF', max_digits=65, decimal_places=0)  # Field name made lowercase.
    tf = models.DecimalField(db_column='TF', max_digits=65, decimal_places=0)  # Field name made lowercase.
    blk = models.DecimalField(db_column='BLK', max_digits=65, decimal_places=0)  # Field name made lowercase.
    bpg = models.DecimalField(db_column='BPG', max_digits=65, decimal_places=4)  # Field name made lowercase.
    to = models.DecimalField(db_column='TO', max_digits=65, decimal_places=0)  # Field name made lowercase.
    stl = models.DecimalField(db_column='STL', max_digits=65, decimal_places=0)  # Field name made lowercase.
    spg = models.DecimalField(db_column='SPG', max_digits=65, decimal_places=4)  # Field name made lowercase.
    oreb = models.DecimalField(db_column='OREB', max_digits=65, decimal_places=0)  # Field name made lowercase.
    dreb = models.DecimalField(db_column='DREB', max_digits=65, decimal_places=0)  # Field name made lowercase.
    rpg = models.DecimalField(db_column='RPG', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sec = models.DecimalField(db_column='SEC', max_digits=65, decimal_places=0)  # Field name made lowercase.
    playedpct = models.DecimalField(db_column='playedPCT', max_digits=24, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_standing_player_23'
        unique_together = (('player', 'league'),)


class SwipsStandingPlayer26Bat(models.Model):
    player = models.PositiveIntegerField(primary_key=True)
    team = models.IntegerField(blank=True, null=True)
    league = models.IntegerField()
    avg = models.DecimalField(db_column='AVG', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obp = models.DecimalField(db_column='OBP', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    slg = models.DecimalField(db_column='SLG', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ops = models.DecimalField(db_column='OPS', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ab = models.DecimalField(db_column='AB', max_digits=65, decimal_places=0)  # Field name made lowercase.
    r = models.DecimalField(db_column='R', max_digits=65, decimal_places=0)  # Field name made lowercase.
    hr = models.DecimalField(db_column='HR', max_digits=65, decimal_places=0)  # Field name made lowercase.
    rbi = models.DecimalField(db_column='RBI', max_digits=65, decimal_places=0)  # Field name made lowercase.
    bb = models.DecimalField(db_column='BB', max_digits=65, decimal_places=0)  # Field name made lowercase.
    so = models.DecimalField(db_column='SO', max_digits=65, decimal_places=0)  # Field name made lowercase.
    sb = models.DecimalField(db_column='SB', max_digits=65, decimal_places=0)  # Field name made lowercase.
    h = models.DecimalField(db_column='H', max_digits=65, decimal_places=0)  # Field name made lowercase.
    sech = models.DecimalField(db_column='SECH', max_digits=65, decimal_places=0)  # Field name made lowercase.
    secf = models.DecimalField(db_column='SECF', max_digits=65, decimal_places=0)  # Field name made lowercase.
    hbp = models.DecimalField(db_column='HBP', max_digits=65, decimal_places=0)  # Field name made lowercase.
    playedpct = models.DecimalField(db_column='playedPCT', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_standing_player_26_bat'
        unique_together = (('player', 'league'),)


class SwipsStandingPlayer26Pit(models.Model):
    player = models.PositiveIntegerField(primary_key=True)
    team = models.IntegerField(blank=True, null=True)
    league = models.IntegerField()
    era = models.DecimalField(db_column='ERA', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    whip = models.DecimalField(db_column='WHIP', max_digits=65, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w = models.DecimalField(db_column='W', max_digits=65, decimal_places=0)  # Field name made lowercase.
    l = models.DecimalField(db_column='L', max_digits=65, decimal_places=0)  # Field name made lowercase.
    outs = models.DecimalField(db_column='OUTS', max_digits=65, decimal_places=0)  # Field name made lowercase.
    nodeci = models.DecimalField(db_column='NODECI', max_digits=65, decimal_places=0)  # Field name made lowercase.
    hold = models.DecimalField(db_column='HOLD', max_digits=65, decimal_places=0)  # Field name made lowercase.
    sv = models.DecimalField(db_column='SV', max_digits=65, decimal_places=0)  # Field name made lowercase.
    svb = models.DecimalField(db_column='SVB', max_digits=65, decimal_places=0)  # Field name made lowercase.
    h = models.DecimalField(db_column='H', max_digits=65, decimal_places=0)  # Field name made lowercase.
    r = models.DecimalField(db_column='R', max_digits=65, decimal_places=0)  # Field name made lowercase.
    er = models.DecimalField(db_column='ER', max_digits=65, decimal_places=0)  # Field name made lowercase.
    bb = models.DecimalField(db_column='BB', max_digits=65, decimal_places=0)  # Field name made lowercase.
    so = models.DecimalField(db_column='SO', max_digits=65, decimal_places=0)  # Field name made lowercase.
    hr = models.DecimalField(db_column='HR', max_digits=65, decimal_places=0)  # Field name made lowercase.
    gp = models.DecimalField(db_column='GP', max_digits=23, decimal_places=0)  # Field name made lowercase.
    gs = models.DecimalField(db_column='GS', max_digits=23, decimal_places=0)  # Field name made lowercase.
    playedpct = models.DecimalField(db_column='playedPCT', max_digits=65, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_standing_player_26_pit'
        unique_together = (('player', 'league'),)


class SwipsStandingTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.IntegerField()
    rank = models.PositiveIntegerField()
    tournament = models.PositiveIntegerField(blank=True, null=True)
    league = models.IntegerField()
    tournament_stage = models.IntegerField(blank=True, null=True)
    standingfk = models.IntegerField(db_column='standingFK')  # Field name made lowercase.
    played = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    wins = models.BigIntegerField(blank=True, null=True)
    draws = models.BigIntegerField(blank=True, null=True)
    defeits = models.BigIntegerField(blank=True, null=True)
    goalsfor = models.BigIntegerField(blank=True, null=True)
    goalsagainst = models.BigIntegerField(blank=True, null=True)
    div = models.CharField(max_length=255)
    conf = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_standing_team'


class SwipsStandingTeam2(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.IntegerField()
    rank = models.PositiveIntegerField()
    tournament = models.PositiveIntegerField(blank=True, null=True)
    league = models.IntegerField()
    tournament_stage = models.IntegerField(blank=True, null=True)
    standingfk = models.IntegerField(db_column='standingFK')  # Field name made lowercase.
    played = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    wins = models.BigIntegerField(blank=True, null=True)
    draws = models.BigIntegerField(blank=True, null=True)
    defeits = models.BigIntegerField(blank=True, null=True)
    goalsfor = models.BigIntegerField(blank=True, null=True)
    goalsagainst = models.BigIntegerField(blank=True, null=True)
    div = models.CharField(max_length=255)
    conf = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_standing_team2'


class SwipsStandingTeamTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.IntegerField()
    rank = models.PositiveIntegerField()
    tournament = models.PositiveIntegerField(blank=True, null=True)
    league = models.IntegerField()
    tournament_stage = models.IntegerField(blank=True, null=True)
    standingfk = models.IntegerField(db_column='standingFK')  # Field name made lowercase.
    played = models.BigIntegerField(blank=True, null=True)
    points = models.BigIntegerField(blank=True, null=True)
    wins = models.BigIntegerField(blank=True, null=True)
    draws = models.BigIntegerField(blank=True, null=True)
    defeits = models.BigIntegerField(blank=True, null=True)
    goalsfor = models.BigIntegerField(blank=True, null=True)
    goalsagainst = models.BigIntegerField(blank=True, null=True)
    div = models.CharField(max_length=255)
    conf = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_standing_team_temp'


class SwipsTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.PositiveIntegerField()
    isnationalteam = models.CharField(db_column='IsNationalTeam', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ut = models.DateTimeField(blank=True, null=True)
    ut2 = models.DateTimeField(blank=True, null=True)
    homepage = models.CharField(db_column='HomePage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    division = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.BigIntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    league = models.IntegerField(blank=True, null=True)
    league_category = models.PositiveIntegerField(blank=True, null=True)
    tournament_stage = models.PositiveIntegerField(blank=True, null=True)
    game_played = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_team'


class SwipsTeamInfo(models.Model):
    team = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mid_name = models.CharField(max_length=30, blank=True, null=True)
    short_name = models.CharField(max_length=5, blank=True, null=True)
    name_ko = models.CharField(max_length=50, blank=True, null=True)
    mid_name_ko = models.CharField(max_length=30, blank=True, null=True)
    name_th = models.CharField(max_length=50, blank=True, null=True)
    mid_name_th = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)
    last_rank = models.CharField(max_length=30, blank=True, null=True)
    no_champions = models.IntegerField(blank=True, null=True)
    manager = models.CharField(max_length=50, blank=True, null=True)
    manager_ko = models.CharField(max_length=50, blank=True, null=True)
    manager_th = models.CharField(max_length=50, blank=True, null=True)
    social = models.CharField(max_length=255, blank=True, null=True)
    social_ko = models.CharField(max_length=255, blank=True, null=True)
    social_pt = models.CharField(max_length=255, blank=True, null=True)
    social_id = models.CharField(max_length=255, blank=True, null=True)
    social_th = models.CharField(max_length=255, blank=True, null=True)
    social_vi = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'swips_team_info'


class SwipsTransfer(models.Model):
    sport = models.IntegerField()
    player_id = models.IntegerField()
    player_name = models.CharField(max_length=45, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    from_team_id = models.IntegerField()
    from_team_name = models.CharField(max_length=45, blank=True, null=True)
    to_team_id = models.IntegerField()
    to_team_name = models.CharField(max_length=45, blank=True, null=True)
    is_loan = models.IntegerField()
    type = models.CharField(max_length=8)
    source_id = models.CharField(max_length=255, blank=True, null=True)
    source_th = models.CharField(max_length=255, blank=True, null=True)
    source_pt = models.CharField(max_length=255, blank=True, null=True)
    source_ko = models.CharField(max_length=255, blank=True, null=True)
    source_vi = models.CharField(max_length=255, blank=True, null=True)
    source_en = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()
    contract_dt = models.DateField()
    contract_info = models.CharField(max_length=8)
    fee = models.BigIntegerField()
    fee_info = models.CharField(max_length=8)
    fee_currency = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'swips_transfer'


class SwipsUser(models.Model):
    device_id = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    user_token = models.CharField(max_length=45, blank=True, null=True)
    fb_user_id = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    data_level = models.IntegerField(blank=True, null=True)
    following_noti_level = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=25, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    push_key = models.CharField(max_length=1023, blank=True, null=True)
    aws_endpoint = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'swips_user'


class SwipsUserBase(models.Model):
    id = models.IntegerField(primary_key=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=25, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    push_key = models.CharField(max_length=1023, blank=True, null=True)
    aws_endpoint = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'swips_user_base'


class SwipsUserFollowing(models.Model):
    user_id = models.IntegerField(primary_key=True)
    following = models.IntegerField()
    type = models.CharField(max_length=2)
    dt = models.DateTimeField()
    aws_subscription = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=5)
    push_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'swips_user_following'
        unique_together = (('user_id', 'following', 'type', 'language', 'push_type'),)


class SwipsUserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    pf = models.CharField(max_length=8, blank=True, null=True)
    pf_user_id = models.CharField(max_length=50, blank=True, null=True)
    pf_user_name = models.CharField(max_length=64, blank=True, null=True)
    pf_user_token = models.CharField(max_length=2048, blank=True, null=True)
    pf_image_url = models.CharField(max_length=255, blank=True, null=True)
    email_confirmed = models.CharField(max_length=3, blank=True, null=True)
    secret_key = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_user_info'
        unique_together = (('user_id', 'pf', 'pf_user_id'),)


class SwipsUserTs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_info_id = models.IntegerField()
    login_ut = models.DateTimeField(blank=True, null=True)
    logout_ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_user_ts'

class CurryVod(models.Model):
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True)
    link = models.CharField(unique=True, max_length=255, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    is_top = models.IntegerField(blank=True, null=True)
    sport = models.IntegerField(blank=True, null=True)
    country_cd = models.CharField(max_length=2, blank=True, null=True)
    language_cd = models.CharField(max_length=2, blank=True, null=True)
    title = models.CharField(max_length=127, blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    following_desc = models.CharField(max_length=255, blank=True, null=True)
    is_frifee_content = models.IntegerField(blank=True, null=True)
    pushed = models.IntegerField()
    country_exclude_cd = models.CharField(max_length=45, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    is_live = models.IntegerField()
    pl_relation = models.CharField(max_length=255, blank=True, null=True)
    te_relation = models.CharField(max_length=255, blank=True, null=True)
    le_relation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curry_vod'
        verbose_name = "VOD"
        verbose_name_plural = "VOD"
class SwipsVod(models.Model):
    id = models.IntegerField(primary_key=True)
    match_id = models.IntegerField(blank=True, null=True)
    link = models.CharField(unique=True, max_length=255, blank=True, null=True)
    image_link = models.CharField(max_length=255, blank=True, null=True)
    create_tmp = models.DateTimeField(blank=True, null=True)
    is_top = models.IntegerField(blank=True, null=True)
    sport = models.IntegerField(blank=True, null=True)
    country_cd = models.CharField(max_length=2, blank=True, null=True)
    language_cd = models.CharField(max_length=2, blank=True, null=True)
    title = models.CharField(max_length=127, blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    following_desc = models.CharField(max_length=255, blank=True, null=True)
    is_frifee_content = models.IntegerField(blank=True, null=True)
    pushed = models.IntegerField()
    country_exclude_cd = models.CharField(max_length=45, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    is_live = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'swips_vod'


class SwipsVodRelation(models.Model):
    participant = models.IntegerField(primary_key=True)
    vod_id = models.IntegerField()
    tmp = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swips_vod_relation'
        unique_together = (('participant', 'vod_id'),)


class TempTu02User(models.Model):
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_tu02_user'


class ThompsonImageSourcePlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    license = models.CharField(max_length=30, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thompson_image_source_player'


class ThompsonStandingColorInfo(models.Model):
    league = models.IntegerField()
    rank = models.IntegerField()
    color_type = models.IntegerField()
    ut = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thompson_standing_color_info'


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    tournament_templatefk = models.PositiveIntegerField(db_column='tournament_templateFK')  # Field name made lowercase.
    enetseasonid = models.PositiveIntegerField(db_column='enetSeasonID')  # Field name made lowercase.
    n = models.PositiveIntegerField()
    locked = models.CharField(max_length=4, blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'tournament'


class TournamentStage(models.Model):
    name = models.CharField(max_length=255)
    tournamentfk = models.PositiveIntegerField(db_column='tournamentFK')  # Field name made lowercase.
    gender = models.CharField(max_length=9)
    countryfk = models.IntegerField(db_column='countryFK')  # Field name made lowercase.
    enetid = models.PositiveIntegerField(db_column='enetID')  # Field name made lowercase.
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    n = models.PositiveIntegerField()
    locked = models.CharField(max_length=4, blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'tournament_stage'


class TournamentTemplate(models.Model):
    name = models.CharField(max_length=50)
    sportfk = models.PositiveIntegerField(db_column='sportFK')  # Field name made lowercase.
    gender = models.CharField(max_length=9)
    enetid = models.PositiveIntegerField(db_column='enetID')  # Field name made lowercase.
    n = models.PositiveIntegerField()
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'tournament_template'


class Venue(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    countryfk = models.IntegerField(db_column='countryFK', blank=True, null=True)  # Field name made lowercase.
    venue_typefk = models.IntegerField(db_column='venue_typeFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue'


class VenueData(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    venue_data_typefk = models.IntegerField(db_column='venue_data_typeFK')  # Field name made lowercase.
    venuefk = models.IntegerField(db_column='venueFK')  # Field name made lowercase.
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue_data'


class VenueDataType(models.Model):
    name = models.CharField(max_length=50)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue_data_type'


class VenueObject(models.Model):
    object_typefk = models.IntegerField(db_column='object_typeFK')  # Field name made lowercase.
    objectfk = models.IntegerField(db_column='objectFK')  # Field name made lowercase.
    venuefk = models.PositiveIntegerField(db_column='venueFK')  # Field name made lowercase.
    neutral = models.CharField(max_length=3)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue_object'


class VenueType(models.Model):
    name = models.CharField(max_length=50)
    del_field = models.CharField(db_column='del', max_length=3)  # Field renamed because it was a Python reserved word.
    n = models.IntegerField()
    ut = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue_type'


class WorldPeacePor(models.Model):
    round = models.IntegerField()
    tournament = models.IntegerField()
    league = models.IntegerField()
    player = models.IntegerField()
    lineup_type = models.IntegerField()
    position = models.IntegerField()
    rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'world_peace_por'


class WorldPeacePorInfo(models.Model):
    round = models.IntegerField()
    tournament = models.IntegerField()
    league = models.IntegerField()
    por_status = models.CharField(max_length=9, blank=True, null=True)
    round_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_peace_por_info'


class WorldPeacePreview(models.Model):
    match_id = models.IntegerField(primary_key=True)
    match_info = models.CharField(max_length=45, blank=True, null=True)
    team1 = models.IntegerField(blank=True, null=True)
    team2 = models.IntegerField(blank=True, null=True)
    match_date = models.DateTimeField(blank=True, null=True)
    team1_rank = models.CharField(max_length=45, blank=True, null=True)
    team2_rank = models.CharField(max_length=45, blank=True, null=True)
    team1_win = models.IntegerField(blank=True, null=True)
    team2_win = models.IntegerField(blank=True, null=True)
    team1_draw = models.IntegerField(blank=True, null=True)
    team2_draw = models.IntegerField(blank=True, null=True)
    team1_defeit = models.IntegerField(blank=True, null=True)
    team2_defeit = models.IntegerField(blank=True, null=True)
    team1_pts = models.IntegerField(blank=True, null=True)
    team2_pts = models.IntegerField(blank=True, null=True)
    team1_result = models.CharField(max_length=45, blank=True, null=True)
    team2_result = models.CharField(max_length=45, blank=True, null=True)
    team1_goals_per_game = models.FloatField(blank=True, null=True)
    team2_goals_per_game = models.FloatField(blank=True, null=True)
    team1_goals_per_game_5 = models.FloatField(blank=True, null=True)
    team2_goals_per_game_5 = models.FloatField(blank=True, null=True)
    team1_goals_against_per_game = models.FloatField(blank=True, null=True)
    team2_goals_against_per_game = models.FloatField(blank=True, null=True)
    team1_goals_against_per_game_5 = models.FloatField(blank=True, null=True)
    team2_goals_against_per_game_5 = models.FloatField(blank=True, null=True)
    team1_key_player = models.IntegerField(blank=True, null=True)
    team2_key_player = models.IntegerField(blank=True, null=True)
    team1_key_player_goal = models.IntegerField(blank=True, null=True)
    team2_key_player_goal = models.IntegerField(blank=True, null=True)
    team1_key_player_assist = models.IntegerField(blank=True, null=True)
    team2_key_player_assist = models.IntegerField(blank=True, null=True)
    team1_top_player = models.CharField(max_length=45, blank=True, null=True)
    team2_top_player = models.CharField(max_length=45, blank=True, null=True)
    team1_top_player_stat = models.CharField(max_length=45, blank=True, null=True)
    team2_top_player_stat = models.CharField(max_length=45, blank=True, null=True)
    team1_top_player_stat_per = models.CharField(max_length=45, blank=True, null=True)
    team2_top_player_stat_per = models.CharField(max_length=45, blank=True, null=True)
    team1_injuries = models.CharField(max_length=45, blank=True, null=True)
    team2_injuries = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=9)
    type = models.IntegerField()
    league = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'world_peace_preview'


class WorldPeaceStandingPlayerParticipant1(models.Model):
    player = models.IntegerField()
    rank = models.PositiveIntegerField()
    tournament = models.PositiveIntegerField(blank=True, null=True)
    league = models.IntegerField()
    played = models.BigIntegerField()
    goals = models.BigIntegerField()
    assists = models.BigIntegerField()
    team = models.BigIntegerField()
    ycards = models.BigIntegerField()
    cleansheets = models.BigIntegerField()
    conceded = models.BigIntegerField()
    playedlineup = models.BigIntegerField()
    min = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'world_peace_standing_player_participant_1'


class WorldPeicePlayerRecent5Games(models.Model):
    match_id = models.IntegerField(primary_key=True)
    league = models.IntegerField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    player_team = models.IntegerField(blank=True, null=True)
    goal = models.IntegerField(blank=True, null=True)
    assist = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_peice_player_recent_5games'


class WpFixtures(models.Model):
    match = models.IntegerField(unique=True, blank=True, null=True)
    tournament = models.IntegerField(blank=True, null=True)
    league = models.IntegerField(blank=True, null=True)
    round = models.IntegerField(blank=True, null=True)
    team1 = models.IntegerField(blank=True, null=True)
    team2 = models.IntegerField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    p_type = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=9)
    pushed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_fixtures'


class WpInjuries(models.Model):
    player = models.IntegerField(blank=True, null=True)
    match = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_injuries'
        unique_together = (('player', 'match', 'team'),)


class WpKeyPl(models.Model):
    match_id = models.IntegerField()
    team = models.IntegerField()
    player = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    rating = models.FloatField()
    played = models.IntegerField()
    n = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_key_pl'
        unique_together = (('match_id', 'team'),)


class WpTeamStat(models.Model):
    match_id = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    draw = models.IntegerField(blank=True, null=True)
    defeit = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    games = models.IntegerField(blank=True, null=True)
    prev_rank = models.CharField(max_length=32, blank=True, null=True)
    prev_result = models.CharField(max_length=32, blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    goals_re = models.FloatField(blank=True, null=True)
    ga_s = models.IntegerField(blank=True, null=True)
    ga_s_re = models.FloatField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    ratings_re = models.FloatField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_team_stat'
        unique_together = (('match_id', 'team'),)


class WpTopPl(models.Model):
    match_id = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    stat_type = models.CharField(max_length=7, blank=True, null=True)
    stat = models.FloatField(blank=True, null=True)
    avg_stat = models.FloatField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_top_pl'
        unique_together = (('match_id', 'team', 'stat_type'),)


class WpTransfer(models.Model):
    tournament = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    active = models.CharField(max_length=3, blank=True, null=True)
    ut = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'wp_transfer'
        unique_together = (('team', 'player', 'ut'),)
