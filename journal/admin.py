from django.contrib import admin
from .models import Post, Product

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author')
admin.site.register(Post, PostAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)