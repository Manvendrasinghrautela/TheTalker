# Blog Project Deployment Guide

## Overview
This is a Django blog application optimized for deployment on Railway or similar platforms.

## Requirements
- Python 3.10+
- Django 5.1.3
- PostgreSQL (recommended for production)

## Environment Variables
Set these environment variables in your deployment platform:

### Required
- `SECRET_KEY`: Django secret key (generate a new one for production)
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### Optional
- `DATABASE_URL`: PostgreSQL connection string (if not using SQLite)

## Railway Deployment

1. **Connect your repository** to Railway
2. **Set environment variables**:
   ```
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.up.railway.app
   ```
3. **Add PostgreSQL database** (optional but recommended)
4. **Deploy**

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   ```bash
   cp env.example .env
   # Edit .env with your settings
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**:
   ```bash
   python manage.py runserver
   ```

## Security Notes
- Never commit `.env` files
- Use strong secret keys in production
- Enable HTTPS in production
- Regular security updates

## Features
- Blog post management
- Category system
- Image uploads
- Search functionality
- Responsive design



