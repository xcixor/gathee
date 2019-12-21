"""Presents the contacts page."""
from django.shortcuts import render
from subscriptions.application.contact.contact import get_address_info


def contact(request):
    """Render the contacts page."""
    context = {
        'address': get_address_info
    }
    return render(request, 'contact/contact.html', context)
