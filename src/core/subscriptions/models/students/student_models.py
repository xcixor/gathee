"""Contains models associated with students of the academy."""
from django.db import models
from django.utils.translation import gettext_lazy as _
from subscriptions.models.auth.models import User
from subscriptions.models.course.course_models import Course


class Student(models.Model):
    """
    Student model
    """

    class Meta:
        """Additional description."""
        verbose_name_plural = "Register Users for a Course"
        unique_together = ('student', 'course')

    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
    is_allowed = models.BooleanField(
        _('viewing status'), default=False,
        help_text=_(
            'Check to ascertain user can view this course.'
            ),
        )

    def __str__(self):
        return str(self.student) + " - " + str(self.course)
