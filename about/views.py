from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about(request):
    """Render the latest About content."""
    about_obj = About.objects.order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(request, 'about/about.html', {'about': about_obj, 'collaborate_form': collaborate_form})
