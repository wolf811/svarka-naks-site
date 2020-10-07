from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('journal_info', views.journal_info, name='journal_info'),
    path('journal_founders', views.journal_founders, name='journal_founders'),
    path('journal_collegium', views.journal_collegium, name='journal_collegium'),
    path('journal_recentering', views.journal_recentering, name='journal_recentering'),
    path('alyoshin', views.alyoshin, name='alyoshin'),
    path('authors', views.authors, name='authors'),
    path('archive', views.archive, name='archive'),
    path('subscription', views.subscription, name='subscription'),
    path('advertising', views.advertising, name='advertising'),
    path('contacts', views.contacts, name='contacts'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]