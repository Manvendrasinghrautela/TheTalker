import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from blog_app.models import Post
from django.utils.text import slugify

for post in Post.objects.all():
    if not post.slug:
        base_slug = slugify(post.title)
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exclude(pk=post.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        post.slug = slug
        post.save()
