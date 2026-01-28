from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'status', 'created_on')
	search_fields = ('title', 'content')
	list_filter = ('status', 'created_on')
	readonly_fields = ('created_on',)
