"""Fetches about page data."""
from subscriptions.models.tutors.models import Tutor


def get_tutors():
    """
    Fetches academy's tutors

    Returns:
     tutors(list): list of tutors
    """
    tutors = Tutor.objects.all()
    return tutors
