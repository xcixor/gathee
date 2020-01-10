"""
Contains functions for processing information to be displayed
on the courses page.
"""
from django import template
from subscriptions.application.students.students_data import (
    course_student_total)


register = template.Library()


@register.filter
def get_students_total(course_id):
    """Fetch course students total."""
    return course_student_total(course_id)
