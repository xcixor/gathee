"""Contains views related with courses."""
from django.shortcuts import render
from subscriptions.application.courses.courses import courses


def courses_view(request):
    """Renders the courses page."""
    context = {
        'courses': courses(),
    }
    return render(request, 'courses/courses.html', context)
