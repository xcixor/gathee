from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login
from subscriptions.application.auth.forms import LoginForm

def login_request(request):
    """Authenticates user credentials and grants account access."""
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
    return render(request, 'index/index.html', {'form': form})