from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def home(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'journal/home.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'journal/post_detail.html', {'post': post})

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'journal/post_list.html', {'posts': posts})

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

def alyoshin(request):
	title = 'Алёшин Николай Павлович'
	content = {
		'title': title
	}
	return render(request, 'journal/alyoshin.html', content)