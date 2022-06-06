from django.contrib import admin
from .models import Post, Comment, Video
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'id']
    search_fields = ['title', 'author', 'id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post']
    list_filter = ['created', 'updated']
    search_fields = ['name', 'email', 'body']

admin.site.register(Video)





