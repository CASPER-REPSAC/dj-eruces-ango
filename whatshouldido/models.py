# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class GroupArticles(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupid = models.ForeignKey('Studygroups', related_name='id', db_column='groupID',
                                on_delete=models.CASCADE)  # Field name made lowercase.
    userid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='userid')
    grouparticletitle = models.CharField(max_length=64)
    grouparticlecontent = models.CharField(max_length=150)
    grouparticlecategory = models.SmallIntegerField(db_column='groupArticleCategory')  # Field name made lowercase.
    uploaddate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_articles'

    def __str__(self):
        return self.grouparticletitle


class GroupAssignments(models.Model):
    groupid = models.ForeignKey('Studygroups', models.DO_NOTHING, db_column='groupID')  # Field name made lowercase.
    groupassignment = models.CharField(db_column='groupAssignment', max_length=32)  # Field name made lowercase.
    groupassignmentdetail = models.CharField(db_column='groupAssignmentdetail',
                                             max_length=500)  # Field name made lowercase.
    groupassignmentlimit = models.DateTimeField(db_column='groupAssignmentlimit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group_assignments'


class GroupCalendar(models.Model):
    groupid = models.ForeignKey('Studygroups', models.DO_NOTHING, db_column='groupID')  # Field name made lowercase.
    groupplanid = models.AutoField(db_column='groupPlanid', primary_key=True)  # Field name made lowercase.
    groupplanname = models.CharField(db_column='groupPlanname', max_length=64)  # Field name made lowercase.
    groupplaninfo = models.CharField(db_column='groupPlaninfo', max_length=128)  # Field name made lowercase.
    groupplanlink = models.CharField(db_column='groupPlanlink', max_length=200, blank=True, null=True)  # Field name made lowercase.
    groupplandate = models.DateTimeField(db_column='groupPlandate')  # Field name made lowercase.
    groupplantime = models.DateTimeField(db_column='groupPlantime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group_calendar'  # studygroups가 아니라 별개의 테이블이 있음.


class GroupArticleComments(models.Model):
    articleid = models.ForeignKey(GroupArticles, related_name='commentid', db_column='articleid',
                                  on_delete=models.CASCADE)
    commentid = models.AutoField(primary_key=True)
    writer = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='writer')
    comment = models.CharField(max_length=100)
    writedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'grouparticlecomments'  # studygroups가 아니라 별개의 테이블이 있음.


class SocialaccountSocialaccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp_id = models.BigIntegerField()
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp_id', 'site'),)


class SocialaccountSocialtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class Studygroups(models.Model):
    groupid = models.AutoField(db_column='groupID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=64)  # Field name made lowercase.
    grouppasscode = models.CharField(db_column='groupPasscode', max_length=64)  # Field name made lowercase.
    groupmaster = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='groupMaster')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studygroups'

    def __str__(self):
        return self.groupname


class UsersGroupsMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    useridx = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='useridx')
    groupidx = models.ForeignKey(Studygroups, models.DO_NOTHING, db_column='groupidx')

    class Meta:
        managed = False
        db_table = 'users_groups_mapping'
        unique_together = (('id', 'useridx', 'groupidx'),)


class ArticleFiles(models.Model):
    id = models.IntegerField(primary_key=True)
    articleid = models.ForeignKey('GroupArticles', models.DO_NOTHING, db_column='articleid')
    uploader = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='uploader')
    field_native_filename = models.CharField(db_column='_native_filename', max_length=32)  # Field renamed because it started with '_'.
    field_encr_filename = models.CharField(db_column='_encr_filename', unique=True, max_length=64)  # Field renamed because it started with '_'.
    uploaded_date = models.DateTimeField(auto_now = True)
    field_file_size = models.IntegerField(db_column='_file_size')  # Field renamed because it started with '_'.
    field_file_type = models.CharField(db_column='_file_type', max_length=4)  # Field renamed because it started with '_'.
    uploaded_file = models.FileField(upload_to="")

    class Meta:
        managed = False
        db_table = 'article_files'
