"""Presents the about page."""
from django.shortcuts import render
from subscriptions.application.about.about_page_data import get_tutors
from subscriptions.application.students.students_data import students_total
from subscriptions.application.contact.contact import get_address_info


def about_page(request):
    context = {
        'tutors': get_tutors,
        'students_total': students_total,
        'address': get_address_info
    }
    return render(request, 'about/about.html', context)
