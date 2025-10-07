from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.templatetags.static import static as static_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    # Favicon redirect to static SVG to avoid 404s
    path('favicon.ico', RedirectView.as_view(url=static_url('blog_app/favicon.svg'), permanent=True)),
]

# Serve media files in both development and production
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
