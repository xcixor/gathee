from django import forms

class LoginForm(forms.Form):
    """
    Login form
        - Authenticates user agains registered accounts
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
