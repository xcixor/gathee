"""Defines the models for videos."""
from django.db import models
from subscriptions.models.courses.models import Course


class PremiumVideo(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    video_file = models.FileField(upload_to='videos', null=True, verbose_name="Select Video:")
    course = models.ForeignKey(
        Course, related_name='videos', on_delete=models.SET_NULL,
        null=True, blank=True)

    def __str__(self):
        return self.name + ": " + str(self.video_file)


class DemoVideo(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    video_file = models.FileField(upload_to='videos', null=True, verbose_name="Select Video:")

    def __str__(self):
        return self.name


class PremiumVideoDemo(models.Model):
    """Maps a demo to its video."""

    class Meta:
        verbose_name_plural = "Premium Videos Demos"

    demo_video = models.ForeignKey(DemoVideo, on_delete=models.CASCADE, null=False, blank=False)
    premium_video = models.ForeignKey(PremiumVideo, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.demo_video.name + ": " + str(self.demo_video.video_file)


