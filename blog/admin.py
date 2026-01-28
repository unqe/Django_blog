from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'status', 'created_on')
	search_fields = ('title', 'content')
	list_filter = ('status', 'created_on')
	readonly_fields = ('created_on',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('body', 'author', 'post', 'created_on', 'approved')
	search_fields = ('body', 'author__username')
	list_filter = ('approved', 'created_on')
	readonly_fields = ('created_on',)
