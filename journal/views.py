from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category, Product
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

def catalog(request, category_slug=None):
	title = 'Каталог номеров'
	category = None
	categories = Category.objects.all().order_by('num')
	products = Product.objects.filter(public=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	content = {
		'title': title,
		'category': category,
		'categories': categories,
		'products': products
	}
	return render(request, 'journal/catalog.html', content)

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

def basket(request):
	title = 'Корзина'
	content = {
		'title': title
	}
	return render(request, 'journal/basket.html', content)

def user_profile(request):
	title = 'Личный кабинет'
	content = {
		'title': title
	}
	return render(request, 'journal/user_profile.html', content)

def user_subscriptions(request):
	title = 'Личный кабинет'
	content = {
		'title': title
	}
	return render(request, 'journal/user_subscriptions.html', content)