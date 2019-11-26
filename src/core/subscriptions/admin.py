from django.contrib import admin
from subscriptions.models.auth.models import User, CountryCode
from subscriptions.models.video.models import PremiumVideo, DemoVideo, PremiumVideoDemo
from subscriptions.presentation.admin.forms import VideoForm, DemoVideoForm
from subscriptions.models.courses.models import Courses


class PremiumVideoAdmin(admin.ModelAdmin):
    """Defines the video management form for the admin."""
    form = VideoForm

class DemoVideoAdmin(admin.ModelAdmin):
    """Defines the video management form for the admin."""
    form = DemoVideoForm

admin.site.register(User)
admin.site.register(CountryCode)
admin.site.register(PremiumVideo, PremiumVideoAdmin)
admin.site.register(Courses)
admin.site.register(DemoVideo, DemoVideoAdmin)
admin.site.register(PremiumVideoDemo)
