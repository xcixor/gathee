"""Presents the lessons of a course"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from subscriptions.application.video.demo_videos import get_lesson_demo_video
from subscriptions.application.video.lesson_videos import get_lesson_video
from subscriptions.application.lesson.lesson_data import (
    get_lesson, update_viewed_lessons, get_next_lesson)
from subscriptions.application.courses.courses import get_course
from subscriptions.application.students.students_data import get_allowed_student
from subscriptions.application.contact.contact import get_address_info


@login_required
def course_lesson(request, lesson_id):
    """Renders the lesson page."""
    context = fetch_lesson_data(request, lesson_id)
    if context['is_allowed']:
        return render(request, 'lessons/course_lesson.html', context)
    return redirect('/course/{}'.format(context['lesson'].course.pk))


def fetch_lesson_data(request, lesson_id):
    """
    Fetch lesson data
    Args:
        request(object): django request object
        lesson_id(int): lesson primary key

    Returns context(dict): lesson's data
    """
    lesson = get_lesson(lesson_id)
    demo_video = get_lesson_demo_video(lesson)
    video = get_lesson_video(lesson)
    course = get_course(lesson.course.pk)
    lessons = course.lessons.all().order_by('lesson_position')
    is_allowed = False
    next_lesson = None
    if request.user.is_authenticated:
        next_lesson = get_next_lesson(request.user, lesson, course)
        update_viewed_lessons(lesson, request.user)
        student = get_allowed_student(request.user, course)
        if student and student.is_allowed:
            is_allowed = True
    context = {
        'lesson': lesson,
        'demo_video': demo_video,
        'other_lessons': lessons,
        'is_allowed': is_allowed,
        'next': next_lesson,
        'video': video,
        'address': get_address_info
        }
    return context
