
from django.shortcuts import render


def post_list(request):
	# Placeholder view: later we'll implement paginated list of posts
	return render(request, 'blog/post_list.html', {})

# Create your views here.
