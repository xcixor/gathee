"""Fetches lesson related data"""
from subscriptions.models.lesson.lesson_models import Lesson


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
