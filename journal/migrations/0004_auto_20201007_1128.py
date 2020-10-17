# Generated by Django 2.2 on 2020-10-07 08:28

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20201007_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_text',
            field=models.TextField(blank=True, null=True, verbose_name='Краткий текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='full_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полный текст'),
        ),
    ]