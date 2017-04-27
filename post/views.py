from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	categories = Category.objects.filter(publish=True)
	return render(request, 'post/index.html', {'categories': categories})


def about(request):
	return render(request, 'post/about.html')


def contact(request):
	return render(request, 'post/contact.html')

def category(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	posts = Post.objects.filter(publish=True, category=category)
	books = Book.objects.filter(category=category)
	paginator = Paginator(posts, 6)
	page = request.GET.get('page')
	try:
		posts_per_page = paginator.page(page)
	except PageNotAnInteger:
		posts_per_page = paginator.page(1)
	except EmptyPage:
		posts_per_page = paginator.page(paginator.num_pages)
	return render(request, 'post/category.html', {'category': category, 'posts': posts_per_page, 'books': books})


def detail(request, post_slug):
	post = get_object_or_404(Post, slug=post_slug)
	return render(request, 'post/detail.html', {'post': post})
