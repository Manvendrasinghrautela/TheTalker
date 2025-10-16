# blog_app/migrations/0005_post_slug.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_postimage_post'),  # replace with actual last migration before 0005
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
