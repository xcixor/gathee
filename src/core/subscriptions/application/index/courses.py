"""Get Courses."""
from subscriptions.models.courses.models import Courses


def get_courses():
    """Returns a list of courses.

    returns:
        courses(list)
    """
    courses = Courses.objects.all()
    return courses
