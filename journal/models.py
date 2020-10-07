from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок новости', max_length=300)
    short_text = models.TextField(verbose_name='Краткий текст', blank=True, null=True)
    full_text = RichTextUploadingField(verbose_name='Полный текст', blank=True, null=True)
    created_date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    published_date = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title