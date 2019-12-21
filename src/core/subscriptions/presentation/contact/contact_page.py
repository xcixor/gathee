"""Presents the contacts page."""
from django.shortcuts import render

def contact(request):
    """Render the contacts page."""
    return render(request, 'contact/contact.html')