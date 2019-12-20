from django.contrib.auth import logout as auth_logout
from subscriptions.application.auth.forms import LoginForm
from django.shortcuts import redirect
from django.contrib import messages
from subscriptions.application.courses.courses import get_courses
from subscriptions.application.video.demo_videos import get_premium_demo_videos


def logout_request(request):
    """Terminates user session"""
    login_form = LoginForm()
    courses = get_courses()
    demo_videos = get_premium_demo_videos()
    context = {'form': login_form, 'courses': courses, 'demo_videos': demo_videos}
    if request.user:
        auth_logout(request)
        error_message = "Successfuly logged out!"
        messages.error(request, error_message, extra_tags='alert-success alert-dismissible')
        return redirect('/', context)