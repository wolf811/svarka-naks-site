# Generated by Django 2.2.16 on 2020-10-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0021_auto_20201030_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Год'),
        ),
    ]
