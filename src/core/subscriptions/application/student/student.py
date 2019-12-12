"""Fetches student information."""
from subscriptions.models.students.student_models import Student


def student_total(course_id):
    """
    Returns the total number of students for a course.
    """
    total_students = Student.objects.filter(course=course_id).count()
    return total_students