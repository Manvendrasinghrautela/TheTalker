from django.core.management.base import BaseCommand
import os
import shutil
from django.conf import settings

class Command(BaseCommand):
    help = 'Upload media files to the server'

    def handle(self, *args, **options):
        # Create media directory if it doesn't exist
        media_dir = os.path.join(settings.BASE_DIR, 'media', 'post_images')
        os.makedirs(media_dir, exist_ok=True)
        
        # List of sample images to create (since we can't upload files directly)
        sample_images = [
            'timcook.jpg',
            'sam_altman.jpg', 
            'nvidia1.jpg',
            'nvidia3.jpg',
            'hidenburg.jpg',
            'adani.jpg',
            'images.jpg'
        ]
        
        self.stdout.write(f'Created media directory: {media_dir}')
        self.stdout.write('Note: For production, you need to upload your actual image files.')
        self.stdout.write('You can do this by:')
        self.stdout.write('1. Using Railway CLI to copy files')
        self.stdout.write('2. Using a cloud storage service like AWS S3')
        self.stdout.write('3. Adding images through the Django admin interface')
        
        self.stdout.write(
            self.style.SUCCESS('Media directory setup complete!')
        )

