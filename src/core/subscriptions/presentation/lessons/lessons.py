"""Presents the lessons of a course"""
from django.shortcuts import render
from subscriptions.application.video.demo_videos import get_lesson_demo_video
from subscriptions.application.lesson.lesson_data import get_lesson, update_lesson
from subscriptions.application.courses.courses import get_course
from subscriptions.application.students.students_data import get_allowed_student


def course_lesson(request, lesson_id):
    """Renders the lesson page."""
    lesson = get_lesson(lesson_id)
    demo_video = get_lesson_demo_video(lesson)
    course = get_course(lesson.course.pk)
    lessons = course.lessons.all().order_by('lesson_position')
    is_allowed = False
    if request.user.is_authenticated:
        student = get_allowed_student(request.user, course)
        if student and student.is_allowed:
            is_allowed = True
    context = {
        'lesson': lesson,
        'demo_video': demo_video,
        'other_lessons': lessons,
        'is_allowed': is_allowed
        }
    update_lesson(lesson_id, is_viewed=True)
    return render(request, 'lessons/course_lesson.html', context)
