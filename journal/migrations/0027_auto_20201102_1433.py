# Generated by Django 2.2 on 2020-11-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0026_auto_20201102_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='num',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядок вывода'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file_contents',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Добавить файл содержания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='file_contents',
            field=models.FileField(blank=True, null=True, upload_to='products/', verbose_name='Добавить файл содержания'),
        ),
    ]
