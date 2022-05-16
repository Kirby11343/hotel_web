from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type', blank=True, null=True)
    number_of_residents = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room'
        verbose_name = 'Номер'
        verbose_name_plural = 'Номери'


class RoomType(models.Model):
    room_type_title = models.CharField(primary_key=True, max_length=100)
    content = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_type'
        verbose_name = 'Тип номеру'
        verbose_name_plural = 'Тип номерів'

class Price(models.Model):
    numberofpeople = models.IntegerField()
    rate = models.FloatField()
    rate_0 = models.ForeignKey('Rate', models.DO_NOTHING, db_column='rate_id')  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'price'
        verbose_name = 'Ціна'
        verbose_name_plural = 'Ціни'


class Rate(models.Model):
    rate_from_date = models.DateField()
    rate_to_date = models.DateField()
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type')

    class Meta:
        managed = False
        db_table = 'rate'
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифи'

class Block(models.Model):
    block_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='room')
    block_start_date = models.DateField()
    block_finish_date = models.DateField()
    reason = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block'
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'

class Gallery(models.Model):
    room_type_title = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type_title', blank=True, null=True, verbose_name='Назва типу кімнати')
    room_number = models.ForeignKey('Room', models.DO_NOTHING, db_column='room_number', blank=True, null=True, verbose_name='Номер кімнати')
    category_title = models.ForeignKey('Category', models.DO_NOTHING, db_column='category_title', blank=True, null=True, verbose_name='Назва категорії')
    maintenance_title = models.ForeignKey('Maintenance', models.DO_NOTHING, db_column='maintenance_title', blank=True, null=True, verbose_name='Назва обслуговування')
    room_image = models.ImageField(upload_to='gallery/', verbose_name='Зображення', default='gallery/no_image.jpg')

    @property
    def thumbnail_preview(self):
        if self.room_image:
            _thumbnail = get_thumbnail(self.room_image,
                                       '100x100',
                                       upscale=False,
                                       crop=False,
                                       quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        managed = False
        db_table = 'gallery'
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереї'

class Category(models.Model):
    category_title = models.CharField(primary_key=True, max_length=100)
    category_description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Maintenance(models.Model):
    maintenance_title = models.CharField(primary_key=True, max_length=100)
    maintenance_price = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'maintenance'
        verbose_name = 'Обслуговування'
        verbose_name_plural = 'Обслуговування'