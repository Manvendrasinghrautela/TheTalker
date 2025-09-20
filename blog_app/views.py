from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q

def homepage(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog_app/homepage.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=post.pk)[:3]
    return render(request, 'blog_app/article_detail.html', {
        'post': post,
        'related_posts': related_posts
    })

def search_results(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    date = request.GET.get('date', '')
    results = Post.objects.all()
    if query:
        results = results.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if category:
        results = results.filter(category__slug=category)
    if date:
        results = results.filter(created_at__date=date)

    categories = Category.objects.all()  # fetch all categories for dropdown

    return render(request, 'blog_app/search_listing.html', {
        'results': results,
        'query': query,
        'category': category,
        'date': date,
        'categories': categories,  # pass categories to template
    })
