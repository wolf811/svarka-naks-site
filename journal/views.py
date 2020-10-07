from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def home(request):
	title = 'Главная'
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	content = {
		'posts': posts,
		'title': title
	}
	
	return render(request, 'journal/home.html', content)

def post_detail(request, pk):
	title = 'Новость детально'
	post = get_object_or_404(Post, pk=pk)
	content = {
		'post': post,
		'title': title
	}
	
	return render(request, 'journal/post_detail.html', content)

def post_list(request):
	title = 'Новости'
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	content = {
		'posts': posts,
		'title': title
	}
	return render(request, 'journal/post_list.html', content)

def journal_info(request):
	title = 'О журнале'
	content = {
		'title': title
	}
	return render(request, 'journal/journal_info.html', content)

def journal_founders(request):
	title = 'Учредители'
	content = {
		'title': title
	}
	return render(request, 'journal/journal_founders.html', content)

def journal_collegium(request):
	title = 'Редакционная коллегия'
	content = {
		'title': title
	}
	return render(request, 'journal/journal_collegium.html', content)

def journal_recentering(request):
	title = 'Порядок рецензирования'
	content = {
		'title': title
	}
	return render(request, 'journal/journal_recentering.html', content)

def alyoshin(request):
	title = 'Алёшин Николай Павлович'
	content = {
		'title': title
	}
	return render(request, 'journal/alyoshin.html', content)

def authors(request):
	title = 'Авторам'
	content = {
		'title': title
	}
	return render(request, 'journal/authors.html', content)

def archive(request):
	title = 'Архив номеров'
	content = {
		'title': title
	}
	return render(request, 'journal/archive.html', content)

def subscription(request):
	title = 'Подписка'
	content = {
		'title': title
	}
	return render(request, 'journal/subscription.html', content)

def advertising(request):
	title = 'Реклама'
	content = {
		'title': title
	}
	return render(request, 'journal/advertising.html', content)

def contacts(request):
	title = 'Контакты'
	content = {
		'title': title
	}
	return render(request, 'journal/contacts.html', content)