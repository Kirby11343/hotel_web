# Generated by Django 4.0.4 on 2022-05-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата реєстрації')),
                ('is_paid_for', models.BooleanField(verbose_name='Сплачено?')),
                ('is_confirmed', models.BooleanField(verbose_name='Підтверджено?')),
                ('living_start_date', models.DateField(verbose_name='Дата заїду')),
                ('living_finish_date', models.DateField(verbose_name='Дата виїзду')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Коментар')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]