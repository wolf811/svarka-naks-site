# Generated by Django 2.2.16 on 2020-10-30 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0019_auto_20201027_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id',)},
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
