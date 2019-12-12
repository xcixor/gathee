"""Defines the data for the courses page."""
from subscriptions.models.courses.models import Course


def courses():
    """Returns a list of all courses."""
    courses_list = Course.objects.all()
    return courses_list
