# Generated by Django 2.2 on 2020-10-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_auto_20201020_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Добавить фото'),
        ),
    ]
