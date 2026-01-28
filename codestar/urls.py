"""codestar URL configuration.

Maps `/blog/` to the `hello_blog` view in the `blog` app.
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog-urls'),
]
