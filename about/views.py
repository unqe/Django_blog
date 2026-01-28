from django.shortcuts import render
from .models import About


def about(request):
    """Render the latest About content."""
    about_obj = About.objects.order_by('-updated_on').first()
    return render(request, 'about/about.html', {'about': about_obj})
