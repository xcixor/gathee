"""Defines the model for course tutors."""
from django.db import models


class Tutor(models.Model):
    """Tutor model"""
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    surname = models.CharField(max_length=40, null=False, blank=False)
    about_totor = models.CharField(max_length=600, null=False, blank=False)
    tutor_image = models.ImageField(null=True, upload_to="images/courses/")

    def __str__(self):
        if self.first_name and self.surname:
            full_name = '%s %s' % (self.first_name, self.surname)
            return full_name.strip()
        elif self.first_name and self.last_name:
            full_name = '%s %s' % (self.first_name, self.last_name)
            return full_name.strip()
        elif self.surname and self.last_name:
            full_name = '%s %s' % (self.last_name, self.surname)
            return full_name.strip()
        return "{} {}".format(self.first_name, self.last_name)
