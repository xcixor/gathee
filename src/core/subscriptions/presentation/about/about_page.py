"""Presents the about page."""
from django.shortcuts import render
from subscriptions.application.about.about_page_data import get_tutors
from subscriptions.application.students.students_data import students_total


def about_page(request):
    tutors = get_tutors()
    students = students_total()
    context = {
        'tutors': tutors,
        'students_total': students_total
    }
    return render(request, 'about/about.html', context)