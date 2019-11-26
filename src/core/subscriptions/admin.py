from django.contrib import admin
from subscriptions.models.auth.models import User, CountryCode
from subscriptions.models.video.models import Video
from subscriptions.presentation.admin.forms import VideoForm
from subscriptions.models.courses.models import Courses


class VideoAdmin(admin.ModelAdmin):
    """Defines the video management form for the admin."""
    form = VideoForm

admin.site.register(User)
admin.site.register(CountryCode)
admin.site.register(Video, VideoAdmin)
admin.site.register(Courses)