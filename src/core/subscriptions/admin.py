from django.contrib import admin
from subscriptions.models.auth.models import User, CountryCode
from subscriptions.models.video.video_models import (
    PremiumVideo, DemoVideo, PremiumVideoDemo, LessonVideoDemo, LessonVideo)
from subscriptions.application.admin.forms import (
    VideoForm, DemoVideoForm, CoursesForm, AddressForm)
from subscriptions.models.course.course_models import (
    Course, PendingCourseRequest)
from subscriptions.models.tutors.models import Tutor
from subscriptions.models.students.student_models import Student
from subscriptions.models.lesson.lesson_models import Lesson
from subscriptions.models.company.company_models import Address


class PremiumVideoAdmin(admin.ModelAdmin):
    """Defines the video management form for the admin."""
    form = VideoForm


class DemoVideoAdmin(admin.ModelAdmin):
    """Defines the Demo video management form for the admin."""
    form = DemoVideoForm


class CourseAdmin(admin.ModelAdmin):
    """Defines the Course management form for the admin."""
    form = CoursesForm


class AddressForm(admin.ModelAdmin):
    """Collects address info"""
    form = AddressForm


admin.site.register(User)
admin.site.register(CountryCode)
admin.site.register(PremiumVideo, PremiumVideoAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(DemoVideo, DemoVideoAdmin)
admin.site.register(PremiumVideoDemo)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(PendingCourseRequest)
admin.site.register(LessonVideo)
admin.site.register(LessonVideoDemo)
admin.site.register(Address, AddressForm)
