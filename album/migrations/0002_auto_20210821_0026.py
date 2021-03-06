# Generated by Django 3.1.4 on 2021-08-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='url',
            field=models.SlugField(blank=True, default='', max_length=130, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.SlugField(blank=True, max_length=160, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='original_sizes',
            field=models.CharField(blank=True, default='0', max_length=9, verbose_name='Оригинальный размер'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='resized',
            field=models.CharField(blank=True, default='0', max_length=8, verbose_name='Измененный размер'),
        ),
    ]
