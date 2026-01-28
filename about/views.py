from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about(request):
    """Render the latest About content and handle collaboration requests."""

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days.",
            )

    about_obj = About.objects.order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        'about/about.html',
        {'about': about_obj, 'collaborate_form': collaborate_form},
    )
