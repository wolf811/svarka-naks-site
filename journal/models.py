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
    img = models.ImageField(upload_to='images/', verbose_name='Добавить фото', null=True, blank=True)
    img_journal = models.ImageField(upload_to='images/', verbose_name='Добавить фото журнала', null=True, blank=True)

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    @property
    def img_journal_url(self):
        if self.img_journal and hasattr(self.img_journal, 'url'):
            return self.img_journal.url

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title