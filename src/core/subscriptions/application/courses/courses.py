"""Defines the data for the courses page."""
from subscriptions.models.course.course_models import Course, PendingCourseRequest
from django.db import IntegrityError


def get_courses():
    """Returns a list of courses.

    returns:
        courses(list)
    """
    courses_list = Course.objects.all()
    return courses_list


def get_course(course_id):
    """Returns the course specified by id provided."""
    course = Course.objects.get(id=course_id)
    return course

def save_course_request(student, course):
    """
    Args:
        student(user object):user requesting the course
        course(course object): course being requested
    Saves a user course request.
    """
    try:
        PendingCourseRequest.objects.create(student=student,course=course)
        return True
    except IntegrityError as e:
        # log error
        return {"error message":"You have aready registered for this course"}
