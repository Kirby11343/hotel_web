from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

from main.models import AuthUser


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type', blank=True, null=True)
    number_of_residents = models.ForeignKey('Price', models.DO_NOTHING, db_column='number_of_residents')

    class Meta:
        managed = False
        db_table = 'room'
        verbose_name = 'Номер'
        verbose_name_plural = 'Номери'


class RoomType(models.Model):
    room_type_title = models.CharField(primary_key=True, max_length=100, verbose_name='Назва типу кімнати')
    content = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Опис')
    slug = models.SlugField(null=False, unique=True, verbose_name='Slug, шлях /room_type_detail/slug/')

    def __str__(self):
        return self.room_type_title

    def get_absolute_url(self):
        return reverse("room_type_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.room_type_title)
        return super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'room_type'
        verbose_name = 'Тип номеру'
        verbose_name_plural = 'Типи номерів'

class Price(models.Model):
    numberofpeople = models.IntegerField(verbose_name='Кількість осіб')
    rate = models.FloatField(verbose_name='Ціна')
    room_type_fk = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type_fk', blank=True, null=True, verbose_name='Тип кімнати')

    class Meta:
        managed = False
        db_table = 'price'
        unique_together = (('numberofpeople', 'room_type_fk'),)
        verbose_name = 'Ціна'
        verbose_name_plural = 'Ціни'

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
    room_type_title = models.OneToOneField('RoomType', models.DO_NOTHING, db_column='room_type_title', blank=True, null=True, verbose_name='Назва типу кімнати')
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
    category_title = models.CharField(primary_key=True, max_length=100,  verbose_name='Назва категорії')
    category_description = models.CharField(max_length=1000, blank=True, null=True,  verbose_name='Опис категорії')
    slug = models.SlugField(null=False, unique=True, verbose_name='Slug, шлях /category_detail/slug/')

    def __str__(self):
        return self.category_title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.category_title)
        return super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Maintenance(models.Model):
    maintenance_title = models.CharField(primary_key=True, max_length=100,  verbose_name='Назва послуги')
    maintenance_price = models.IntegerField(blank=True, verbose_name='Ціна')
    maintenance_description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Опис послуги')
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', verbose_name='Категорія')
    pdf_file = models.FileField(upload_to='uploads/pdf/', blank=True)


    class Meta:
        managed = False
        db_table = 'maintenance'
        verbose_name = 'Обслуговування'
        verbose_name_plural = 'Обслуговування'

class Order(models.Model):
    maintenance = models.ForeignKey(Maintenance, models.DO_NOTHING, db_column='maintenance', blank=True, null=True, verbose_name='Послуга')
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='room', blank=True, null=True, verbose_name='Номер')
    registration_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата реєстрації')
    id_client = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_client', verbose_name='Id клієнта')
    is_paid_for = models.BooleanField(verbose_name='Сплачено?')
    is_confirmed = models.BooleanField(verbose_name='Підтверджено?')
    living_start_date = models.DateField(verbose_name='Дата заїду')
    living_finish_date = models.DateField(verbose_name='Дата виїзду')
    comment = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Коментар')

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})

    class Meta:
        managed = False
        db_table = 'order'
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
