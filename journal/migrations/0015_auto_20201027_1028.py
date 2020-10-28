# Generated by Django 2.2.16 on 2020-10-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0014_auto_20201026_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
