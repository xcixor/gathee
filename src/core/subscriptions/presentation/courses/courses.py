"""Contains views related with courses."""
from django.shortcuts import render
from subscriptions.application.courses.courses import get_courses, get_course


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
