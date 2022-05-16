# Generated by Django 4.0.4 on 2022-05-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('block_id', models.AutoField(primary_key=True, serialize=False)),
                ('block_start_date', models.DateField()),
                ('block_finish_date', models.DateField()),
                ('reason', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Бронь',
                'db_table': 'block',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category_description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'db_table': 'category',
                'managed': False,
            },
        ),
    
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('maintenance_title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('maintenance_price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Обслуговування',
                'verbose_name_plural': 'Обслуговування',
                'db_table': 'maintenance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberofpeople', models.IntegerField()),
                ('rate', models.FloatField()),
            ],
            options={
                'verbose_name': 'Ціна',
                'verbose_name_plural': 'Ціни',
                'db_table': 'price',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_from_date', models.DateField()),
                ('rate_to_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифи',
                'db_table': 'rate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_residents', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номери',
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('room_type_title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Тип номеру',
                'verbose_name_plural': 'Тип номерів',
                'db_table': 'room_type',
                'managed': False,
            },
        ),
    ]
