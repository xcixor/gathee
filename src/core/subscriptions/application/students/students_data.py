"""Fetches student information."""
from subscriptions.models.students.student_models import Student


def student_total(course_id):
    """
    Returns the total number of students for a course.
    """
    total_students = Student.objects.filter(course=course_id).count()
    return total_students

def get_allowed_student(student, course):
    """
    Fetch registered student

    Args:
        student(object): student to fetch
        course(object): course being requested

    Returns:
        student(object): student's object
    """
    student = Student.objects.filter(student=student, course=course).first()
    return student