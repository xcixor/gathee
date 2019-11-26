"""Get Courses."""
from subscriptions.models.courses.models import Course


def get_courses():
    """Returns a list of courses.

    returns:
        courses(list)
    """
    courses = Course.objects.all()
    return courses
