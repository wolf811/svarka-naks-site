from django.contrib import admin
from .models import Post, Category, Product

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author')
admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'num']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'category', 'created', 'updated', 'public']
    list_filter = ['created', 'updated', 'public']
    list_editable = ['price', 'public']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)