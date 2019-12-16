from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login
from subscriptions.application.auth.forms import LoginForm
from subscriptions.application.courses.courses import get_courses
from subscriptions.application.video.demo_videos import get_demo_videos


def login_request(request):
    """Authenticates user credentials and grants account access."""
    login_form = LoginForm()
    courses = get_courses()
    demo_videos = get_demo_videos()
    context = {'form': login_form, 'courses': courses, 'demo_videos': demo_videos}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                request,
                username=cleaned_data['username'],
                password=cleaned_data['password']
                )
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    next_page = request.POST.get('next')
                    if next_page:
                        return redirect(next_page)
                    return redirect('/')
                else:
                    error_message = "That account has not yet been activated"
                    messages.error(request, error_message, extra_tags='alert-danger alert-dismissible')
                    return redirect('/')
            else:
                error_message = "Invalid username/password combination, Please try Again!"
                messages.error(request, error_message, extra_tags='alert-danger alert-dismissible')
                return redirect('/')
        else:
            error_message = "Invalid Credentials, Please try Again!"
            messages.error(request, error_message, extra_tags='alert-danger alert-dismissible')
            return redirect('/')
    else:
        form = LoginForm()
    msg = "You need to be logged in to perform this action!"
    messages.error(request, msg, extra_tags='alert-danger alert-dismissible')
    return render(request, 'index/index.html', context)