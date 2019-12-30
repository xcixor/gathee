"""Presents the contacts page."""
from django.shortcuts import render, redirect
from django.contrib import messages
from subscriptions.application.contact.contact import get_address_info
from subscriptions.application.contact.forms import ContactForm


def contact(request):
    """Render the contacts page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'address': get_address_info,
            'form': form
        }
        if form.is_valid():
            form.send_email()
            message = "Email sent successfuly!"
            messages.success(
                request,
                message,
                extra_tags='alert-success alert-dismissible')
            return redirect('/contact', context)
        message = "Email not sent, please try again!"
        messages.error(
            request,
            message,
            extra_tags='alert-warning alert-dismissible')
        return render(request, 'contact/contact.html', context)
    form = ContactForm()
    context = {
        'address': get_address_info,
        'form': form
    }
    return render(request, 'contact/contact.html', context)
