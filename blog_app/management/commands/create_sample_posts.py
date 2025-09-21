from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from blog_app.models import Post, Category
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Create sample posts with placeholder images'

    def handle(self, *args, **options):
        # Create categories
        tech_category, created = Category.objects.get_or_create(
            name='Technology',
            defaults={'slug': 'technology'}
        )
        
        business_category, created = Category.objects.get_or_create(
            name='Business',
            defaults={'slug': 'business'}
        )
        
        # Create sample posts
        sample_posts = [
            {
                'title': 'Tim Cook: Apple\'s Vision for the Future',
                'content': 'Tim Cook continues to lead Apple into new territories with innovative products and sustainable business practices.',
                'category': tech_category,
                'featured': True
            },
            {
                'title': 'Sam Altman and the AI Revolution',
                'content': 'Sam Altman\'s leadership at OpenAI has been instrumental in bringing AI to the mainstream.',
                'category': tech_category,
                'featured': False
            },
            {
                'title': 'NVIDIA\'s Dominance in AI Chips',
                'content': 'NVIDIA continues to lead the AI chip market with their innovative GPU technology.',
                'category': tech_category,
                'featured': False
            },
            {
                'title': 'Hindenburg Research: Market Analysis',
                'content': 'Hindenburg Research provides detailed analysis of market trends and company valuations.',
                'category': business_category,
                'featured': False
            },
            {
                'title': 'Adani Group: Business Expansion',
                'content': 'The Adani Group continues to expand its business portfolio across various sectors.',
                'category': business_category,
                'featured': False
            }
        ]
        
        for post_data in sample_posts:
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'content': post_data['content'],
                    'category': post_data['category'],
                    'featured': post_data['featured']
                }
            )
            
            if created:
                self.stdout.write(f'Created post: {post.title}')
            else:
                self.stdout.write(f'Post already exists: {post.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Sample posts created successfully!')
        )
        self.stdout.write('Note: Images will show as "No Image" until you upload actual image files.')

