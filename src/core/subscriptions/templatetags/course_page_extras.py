"""
Contains helper functions for course page.
"""
from django import template
from subscriptions.application.courses.courses import get_course

register = template.Library()


@register.filter
def get_course_duration(course_id):
    """Fetch course students total."""
    course = get_course(course_id)
    lessons = course.lessons.all()
    total_course_microseconds = 0
    for lesson in lessons:
        total_course_microseconds += lesson.get_duration()

    seconds = (total_course_microseconds/1000)%60
    seconds = int(seconds)
    minutes = (total_course_microseconds/(1000*60))%60
    minutes = int(minutes)
    hours = (total_course_microseconds/(1000*60*60))%24
    hours = int(hours)
    days = (total_course_microseconds/(1000*60*60*24))
    days = int(days)
    return "{} days {} hrs {} mins {} seconds".format(days, hours, minutes, seconds)


@register.filter
def get_course_first_lesson_id(course_id):
    """
    Get course first lesson

    Args:
        course_id(str): course id
    Returns:
        lesson_id(int):first lesson id
    """
    course = get_course(course_id)
    lessons = course.lessons.all().order_by('lesson_position')
    if lessons:
        lesson = lessons.first()
        lesson_id = lesson.pk
        return lesson_id
    return None
