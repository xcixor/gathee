"""Fetches lesson related data"""
from subscriptions.models.lesson.lesson_models import Lesson, ViewedLesson
from subscriptions.models.students.student_models import Student


def get_lesson(lesson_id):
    """
    Fetches a lesson

    args:
        lesson_id(string): id

    returns:
        lesson(object): lesson requested
    """
    lesson = Lesson.objects.filter(id=lesson_id).first()
    return lesson


def update_lesson(lesson_id, **kwargs):
    """
    Updates a lesson
    """
    Lesson.objects.filter(id=lesson_id).update(**kwargs)


def update_viewed_lessons(lesson, student):
    """
    Updates viewed lessons.
    Args:
        lesson(object): lesson to be updated
        student(object): user who has viewed the lesson
    """
    ViewedLesson.objects.update_or_create(
        lesson=lesson, student=student, is_viewed=True
        )


def get_next_lesson(student, lesson, course):
    """
    Returns next lesson

    Args:
        lesson(object): lesson to be updated
        student(object): user with acccess to course
        course(object): course with next lesson

    Returns:
        next_lesson(object): the next object
    """
    if not Student.objects.filter(student=student).exists():
        return False
    position = lesson.lesson_position + 1
    if not Lesson.objects.filter(lesson_position=position, course=course).exists():
        return False
    next_lesson = Lesson.objects.filter(lesson_position=position, course=course).first()
    return next_lesson
