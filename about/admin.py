from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About
from .models import CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'updated_on')
    ordering = ('-updated_on',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "read", "created_on")
    list_filter = ("read",)
    search_fields = ("name", "email", "message")
