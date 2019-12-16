"""Contains views related with courses."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from subscriptions.application.courses.courses import (
    get_courses, get_course, save_course_request)


def courses_view(request):
    """Renders the courses page."""
    context = {
        'courses': get_courses(),
    }
    return render(request, 'courses/courses.html', context)


def go_to_course(request, course_id):
    """
    Navigates to individual course page
    """
    course = get_course(course_id)
    lessons = course.lessons.all()
    context = {
        'course': course,
        'lessons': lessons
        }
    return render(request, 'courses/course.html', context)


@login_required
def send_course_request(request, course_id):
    """
    Sends a user request to join a course
    """
    user = request.user
    course = get_course(course_id)
    if request.method == 'POST':
        if save_course_request(user, course) == True:
            return render(request, 'courses/course_purchase_confirmation.html', {'course': course})
        error = save_course_request(user, course)['error message']
        messages.error(request, error, extra_tags='alert-danger alert-dismissible')
        return redirect('/purchase_course/{}'.format(course_id))
    return render(request, 'courses/course_purchase.html', {'course': course})


