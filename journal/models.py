from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.urls import reverse

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
    file_contents = models.FileField(upload_to='uploads/', verbose_name='Добавить файл содержания', null=True, blank=True)

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

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    num = models.SmallIntegerField(verbose_name='Порядок вывода', blank=True, null=True, default=0)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('journal:archive_by_category',
    #                     args=[self.slug])

class Product(models.Model):
    # category = models.OneToOneField(Category, related_name='products', on_delete=models.CASCADE, primary_key = True)
    category = models.ForeignKey(Category, related_name='products', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True)
    file_contents = models.FileField(upload_to='products/', verbose_name='Добавить файл содержания', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    public = models.BooleanField(u'Опубликовать', default = True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.name