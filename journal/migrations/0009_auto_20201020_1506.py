# Generated by Django 2.2 on 2020-10-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_auto_20201020_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/', verbose_name='Добавить фото'),
        ),
    ]