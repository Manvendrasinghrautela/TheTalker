from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Category
from django.db.models import Q


def homepage(request):
    posts = Post.objects.order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'blog_app/homepage.html', {
        'posts': posts,
        'categories': categories,
        'current_category': None,
        'page_title': 'All Articles'
    })


def post_detail(request, pk=None, slug=None):
    if slug is not None:
        post = get_object_or_404(Post, slug=slug)
    elif pk is not None:
        post = get_object_or_404(Post, pk=pk)
    else:
        raise Http404("No post found")

    related = Post.objects.filter(category=post.category).exclude(pk=post.pk)[:4]
    posts = Post.objects.exclude(pk=post.pk).order_by('-created_at')[:10]
    categories = Category.objects.all()
    return render(request, 'blog_app/article_detail.html', {
        'post': post,
        'related': related,
        'posts': posts,
        'categories': categories
    })


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'blog_app/homepage.html', {
        'posts': posts,
        'categories': categories,
        'current_category': category,
        'page_title': f'{category.name} Articles'
    })


def search_results(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    date = request.GET.get('date', '')
    results = Post.objects.all().order_by('-created_at')

    if query:
        results = results.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if category:
        results = results.filter(category__slug=category)
    if date:
        results = results.filter(created_at__date=date)

    categories = Category.objects.all()

    return render(request, 'blog_app/search_listing.html', {
        'results': results,
        'query': query,
        'category': category,
        'date': date,
        'categories': categories,
    })
