from django.contrib import admin
from subscriptions.models.auth.models import User, CountryCode
from subscriptions.models.video.models import PremiumVideo, DemoVideo, PremiumVideoDemo
from subscriptions.application.admin.forms import VideoForm, DemoVideoForm, CoursesForm
from subscriptions.models.course.course_models import Course, PendingCourseRequest
from subscriptions.models.tutors.models import Tutor
from subscriptions.models.students.student_models import Student
from subscriptions.models.lesson.lesson_models import Lesson


class PremiumVideoAdmin(admin.ModelAdmin):
    """Defines the video management form for the admin."""
    form = VideoForm

class DemoVideoAdmin(admin.ModelAdmin):
    """Defines the Demo video management form for the admin."""
    form = DemoVideoForm

class CourseAdmin(admin.ModelAdmin):
    """Defines the Course management form for the admin."""
    form = CoursesForm


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
