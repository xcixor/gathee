"""Defines the models for Courses."""
from django.db import models
from subscriptions.models.tutors.models import Tutor


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
