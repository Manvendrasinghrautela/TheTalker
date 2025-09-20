from django.contrib import admin
from .models import Post, Category, PostImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1  # number of extra blank image forms

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'created_at')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'content')
    inlines = [PostImageInline]
