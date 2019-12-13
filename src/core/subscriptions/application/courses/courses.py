"""Defines the data for the courses page."""
from subscriptions.models.courses.models import Course


def get_courses():
    """Returns a list of all courses."""
    courses_list = Course.objects.all()
    return courses_list


def get_course(course_id):
    """Returns the course specified by id provided."""
    course = Course.objects.get(id=course_id)
    return course
