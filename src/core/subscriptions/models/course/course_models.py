"""Defines the models for Courses."""
from django.db import models
from subscriptions.models.tutors.models import Tutor
from subscriptions.models.auth.models import User
from django.contrib.auth.decorators import login_required


class Course(models.Model):
    """Course model."""
    title = models.CharField(max_length=40, null=False, blank=False, unique=True)
    level = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    course_image = models.ImageField(null=True, upload_to="images/courses/")
    price = models.IntegerField(null=True, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self):
        if self.level:
            return "{}: {}".format(self.title, self.level)
        return "{}: {}".format(self.title, "Beginner")


class PendingCourseRequest(models.Model):
    """Contains users pending request to join a course."""

    class Meta:
        """Additional description."""
        verbose_name_plural = "View users who have sent request to join courses"
        unique_together = ('student', 'course')

    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.student) + " : " + str(self.course)

