"""Contains models associated with a course lesson."""
from django.db import models
from subscriptions.models.course.course_models import Course
from django.utils.translation import gettext_lazy as _
from django.utils.duration import _get_duration_components


class Lesson(models.Model):
    """
    Lesson model.
    """
    title = models.CharField(max_length=40, null=False, blank=False, unique=True)
    description = models.CharField(max_length=40, null=False, blank=False, unique=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='lessons'
        )
    duration = models.DurationField(
        null=False,
        blank=False,
        default='00:00:00',
        verbose_name=_('timeslot_duration'),
        help_text=_('[DD (days)] (leave a space between day \
            and hour min sec) [HH:[MM:]]ss[.uuuuuu] format')
        )

    class Meta:
        verbose_name_plural = "Add lessons for courses"


    def get_duration(self):
        """Returns duration string."""
        total_duration_in_microseconds = 0
        days, hours, minutes, seconds, microseconds = _get_duration_components(self.duration)
        total_duration_in_microseconds = ((24*days) * 60 * 60 * 1000) + \
                                        (hours * 60 * 60 * 1000) + \
                                        (minutes * 60 * 1000) + (seconds * 1000) + \
                                         microseconds
        return total_duration_in_microseconds

    def __str__(self):
        return self.title + ' - ' + str(self.course)
