# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    role = models.CharField(max_length=100, blank=True, null=True)

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
    category_price = models.FloatField()

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
    maintenance_type = models.CharField(max_length=100)
    maintenance_price = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'maintenance'


class ModificationHistory(models.Model):
    id_modif = models.AutoField(primary_key=True)
    modif_author = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modif_author')
    modif_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modification_history'


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
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='role', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_type'


class Order(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='room', blank=True, null=True)
    client = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='client', blank=True, null=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    is_paid_for = models.BooleanField()
    is_confirmed = models.BooleanField()
    living_start_date = models.DateField()
    living_finish_date = models.DateField()
    comment = models.CharField(max_length=1000, blank=True, null=True)
    last_modification = models.ForeignKey(ModificationHistory, models.DO_NOTHING, db_column='last_modification', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Phone(models.Model):
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone'


class Price(models.Model):
    numberofpeople = models.IntegerField()
    rate = models.FloatField()
    rate_0 = models.ForeignKey('Rate', models.DO_NOTHING, db_column='rate_id')  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'price'


class Rate(models.Model):
    rate_from_date = models.DateField()
    rate_to_date = models.DateField()
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type')

    class Meta:
        managed = False
        db_table = 'rate'


class Reviews(models.Model):
    author = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='author')
    content = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Role(models.Model):
    role_name = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'role'


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type', blank=True, null=True)
    number_of_residents = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room'


class RoomType(models.Model):
    room_type_title = models.CharField(primary_key=True, max_length=100)
    content = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_type'
