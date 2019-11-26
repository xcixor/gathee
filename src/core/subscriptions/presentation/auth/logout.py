from django.contrib.auth import logout as auth_logout
from subscriptions.application.auth.forms import LoginForm
from django.shortcuts import redirect
from django.contrib import messages


def logout_request(request):
    """Terminates user session"""
    login_form = LoginForm()
    context = {'form': login_form}
    if request.user:
        auth_logout(request)
        error_message = "Successfuly logged out!"
        messages.error(request, error_message, extra_tags='alert-success alert-dismissible')
        return redirect('/', context)