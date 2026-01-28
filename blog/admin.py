from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
	list_display = ('title', 'slug', 'status', 'created_on')
	search_fields = ['title']
	list_filter = ('status',)
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('body', 'author', 'post', 'created_on', 'approved')
	search_fields = ('body', 'author__username')
	list_filter = ('approved', 'created_on')
	readonly_fields = ('created_on',)
