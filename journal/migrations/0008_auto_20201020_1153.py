# Generated by Django 2.2 on 2020-10-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Добавить фото'),
        ),
    ]
