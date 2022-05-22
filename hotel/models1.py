# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


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


class Block(models.Model):
    block_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='room')
    block_start_date = models.DateField()
    block_finish_date = models.DateField()
    reason = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block'


class Category(models.Model):
    category_title = models.CharField(primary_key=True, max_length=100)
    category_description = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Gallery(models.Model):
    room_type_title = models.OneToOneField('RoomType', models.DO_NOTHING, db_column='room_type_title', blank=True, null=True)
    room_number = models.ForeignKey('Room', models.DO_NOTHING, db_column='room_number', blank=True, null=True)
    category_title = models.ForeignKey(Category, models.DO_NOTHING, db_column='category_title', blank=True, null=True)
    maintenance_title = models.ForeignKey('Maintenance', models.DO_NOTHING, db_column='maintenance_title', blank=True, null=True)
    room_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'gallery'


class JournalRecord(models.Model):
    maintenance = models.ForeignKey('Maintenance', models.DO_NOTHING, db_column='maintenance')
    count = models.IntegerField()
    cost = models.IntegerField()
    used_date = models.DateTimeField(blank=True, null=True)
    order = models.ForeignKey('Order', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'journal_record'


class Maintenance(models.Model):
    maintenance_title = models.CharField(primary_key=True, max_length=100)
    maintenance_price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')
    pdf_file = models.CharField(max_length=-1, blank=True, null=True)
    maintenance_description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance'


class Notification(models.Model):
    author = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='author', blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    notification_type = models.ForeignKey('NotificationType', models.DO_NOTHING, db_column='notification_type', blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    send_date = models.DateTimeField(blank=True, null=True)
    executed_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='executed_by', blank=True, null=True)
    executed_date = models.DateField(blank=True, null=True)
    order = models.ForeignKey('Order', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'


class NotificationType(models.Model):
    notif_type_title = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'notification_type'


class Order(models.Model):
    maintenance = models.ForeignKey(Maintenance, models.DO_NOTHING, db_column='maintenance', blank=True, null=True)
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='room', blank=True, null=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    is_paid_for = models.BooleanField()
    is_confirmed = models.BooleanField()
    living_start_date = models.DateField()
    living_finish_date = models.DateField()
    comment = models.CharField(max_length=1000, blank=True, null=True)
    id_client = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_client')

    class Meta:
        managed = False
        db_table = 'order'


class Price(models.Model):
    numberofpeople = models.IntegerField()
    rate = models.FloatField()
    room_type_fk = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'
        unique_together = (('numberofpeople', 'room_type_fk'),)


class Reviews(models.Model):
    author = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='author')
    content = models.CharField(max_length=1000, blank=True, null=True)
    timestamp_review = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type', blank=True, null=True)
    number_of_residents = models.ForeignKey(Price, models.DO_NOTHING, db_column='number_of_residents')

    class Meta:
        managed = False
        db_table = 'room'


class RoomType(models.Model):
    room_type_title = models.CharField(primary_key=True, max_length=100)
    content = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'room_type'


class SocialaccountSocialaccount(models.Model):
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
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class ThumbnailKvstore(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'thumbnail_kvstore'
