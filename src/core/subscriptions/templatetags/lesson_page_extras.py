"""
Contains functions for more control over information displayed
on the lessons page
"""
from django import template
from subscriptions.models.lesson.lesson_models import ViewedLesson


register = template.Library()


@register.filter
def check_viewed(lesson, student):
    """
    Checks whether a student has watched a lessons

    Args:
        lesson(object): the lesson to check
        student(object): active user
    Returns
        Boolean: true if watched, false if not
    """
    if student.is_authenticated:
        viewed_lesson = ViewedLesson.objects.filter(
            lesson=lesson, student=student).first()
        if viewed_lesson and viewed_lesson.is_viewed:
            return True
    return False
