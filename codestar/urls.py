"""codestar URL configuration.

Maps `/blog/` to the `hello_blog` view in the `blog` app.
"""

from django.contrib import admin
from django.urls import path

from blog.views import hello_blog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', hello_blog),
]
