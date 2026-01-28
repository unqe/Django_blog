
from django.views import generic
from .models import Post


class PostList(generic.ListView):
	queryset = Post.objects.filter(author=1)
	template_name = "blog/post_list.html"

# Create your views here.
