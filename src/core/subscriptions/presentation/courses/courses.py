"""Contains views related with courses."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from subscriptions.application.courses.courses import (
    get_courses, get_course, save_course_request)
from subscriptions.application.students.students_data import (
    get_allowed_student)


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
    lessons = course.lessons.all().order_by('lesson_position')
    is_allowed = False
    if request.user.is_authenticated:
        student = get_allowed_student(request.user, course)
        if student and student.is_allowed:
            is_allowed = True
    context = {
        'course': course,
        'lessons': lessons,
        'is_allowed': is_allowed
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
        request_status = save_course_request(user, course)
        if request_status is True:
            return render(request, 'courses/course_purchase_confirmation.html', {'course': course})
        error = request_status['error message']
        messages.error(request, error, extra_tags='alert-danger alert-dismissible')
        return redirect('/purchase_course/{}'.format(course_id))
    return render(request, 'courses/course_purchase.html', {'course': course})
