"""Contains models associated with students of the academy."""
from django.db import models
from subscriptions.models.auth.models import User
from subscriptions.models.courses.models import Course


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

    def __str__(self):
        return str(self.student)


