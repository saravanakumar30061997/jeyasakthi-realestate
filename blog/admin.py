from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # Corrected placement

admin.site.register(Blog, BlogAdmin)  # Register with custom admin class
