from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('journal_info/', views.journal_info, name='journal_info'),
    path('journal_founders/', views.journal_founders, name='journal_founders'),
    path('journal_collegium/', views.journal_collegium, name='journal_collegium'),
    path('journal_recentering/', views.journal_recentering, name='journal_recentering'),
    path('alyoshin/', views.alyoshin, name='alyoshin'),
    path('authors/', views.authors, name='authors'),
    path('catalog/', views.catalog, name='catalog'),
    # path('catalog/<category_slug>/', views.catalog, name='catalog_by_category'),
    path('subscription/', views.subscription, name='subscription'),
    path('advertising/', views.advertising, name='advertising'),
    path('contacts/', views.contacts, name='contacts'),
    path('basket/', views.basket, name='basket'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_subscriptions/', views.user_subscriptions, name='user_subscriptions'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)