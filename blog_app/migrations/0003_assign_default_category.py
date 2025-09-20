from django.db import migrations


def assign_default_category(apps, schema_editor):
    Category = apps.get_model('blog_app', 'Category')
    Post = apps.get_model('blog_app', 'Post')

    default_category = Category.objects.get(pk=1)

    Post.objects.filter(category__isnull=True).update(category=default_category)


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_postimage'),
    ]

    operations = [
        migrations.RunPython(assign_default_category),
    ]
