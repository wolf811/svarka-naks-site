# Generated by Django 2.2 on 2020-11-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0029_auto_20201103_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
    ]
