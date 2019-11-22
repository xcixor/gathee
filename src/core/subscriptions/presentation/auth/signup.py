from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login as auth_login
from subscriptions.models.auth.models import CountryCode


def signup_view(request):
    """
    Renders the signup page and allows the user to create an account
        by providing the required details.
    """
    codes = CountryCode.objects.all()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            return redirect('/account')
        else:
            return render(request, 'auth/signup.html', {'form': form, 'codes': codes})
    registration_form = UserRegistrationForm()
    context = {'form': registration_form, 'codes': codes}
    return render(request, 'auth/signup.html', context)
