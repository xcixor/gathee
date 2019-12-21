from django.shortcuts import render, redirect
from subscriptions.application.auth.forms import UserRegistrationForm
from django.contrib.auth import login as auth_login
from subscriptions.application.auth.auth_data import get_country_codes
from subscriptions.application.contact.contact import get_address_info


def signup_view(request):
    """
    Renders the signup page and allows the user to create an account
        by providing the required details.
    """
    codes = get_country_codes()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            return redirect('/account')
        else:
            return render(request, 'auth/signup.html', {
                'form': form, 'codes': codes, 'address': get_address_info})
    registration_form = UserRegistrationForm()
    context = {
        'form': registration_form,
        'codes': codes,
        'address': get_address_info
        }
    return render(request, 'auth/signup.html', context)
