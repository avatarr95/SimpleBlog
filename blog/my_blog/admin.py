from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'author')
    date_hierarchy = ('updated')
    prepopulated_fields = {
        'slug': ('title',)
    }
