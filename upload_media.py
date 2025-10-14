#!/usr/bin/env python
"""
Script to upload media files to Railway deployment
"""
import os
import subprocess
import sys

def upload_media_files():
    """Upload media files to Railway"""
    media_dir = "media/post_images"
    
    if not os.path.exists(media_dir):
        print(f"Media directory {media_dir} not found!")
        return False
    
    print("Uploading media files to Railway...")
    
    # List all files in media directory
    files = os.listdir(media_dir)
    print(f"Found {len(files)} files to upload:")
    for file in files:
        print(f"  - {file}")
    
    # Use railway CLI to upload files
    try:
        # Create a tar archive of media files
        subprocess.run([
            "tar", "-czf", "media_files.tar.gz", "-C", "media", "post_images"
        ], check=True)
        
        print("Media files archived successfully!")
        print("You can now deploy this to Railway and the images will be available.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating archive: {e}")
        return False
    
    return True

if __name__ == "__main__":
    upload_media_files()



