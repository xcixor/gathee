import re
from django import forms
from subscriptions.models.auth.models import User, CountryCode, get_default
from subscriptions.utils.twilio import TwilioValidation


class LoginForm(forms.Form):
    """
    Login form
        - Authenticates user agains registered accounts
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    Registration form
        - Collects user information for account creation
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'firstname', 'lastname', 'surname', 'phone_number')

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    # country_codes = CountryCode.objects.all()
    # CHOICE_LIST = []
    # for code in country_codes:
    #     CHOICE_LIST.append((code.country, code))
    # country_code = forms.ChoiceField(choices=CHOICE_LIST,
    #                                  widget=forms.Select(
    #                                      attrs={'class':'custom-select'}))


    def clean_password2(self):
        """
        Validate passwords match
        """
        cleaned_data = self.cleaned_data
        password = cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password must be more than eight characters')
        elif re.search('[0-9]',password) is None:
            raise forms.ValidationError('Make sure your password has a number in it')
        # elif re.search('[A-Z]+[a-z]',password) is None:
        #     raise forms.ValidationError('Password must mix uppercase and lowercase characters')
        # elif re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None:
        #     raise forms.ValidationError('Password must have atleast one special character')
        if password != cleaned_data['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cleaned_data['password2']

    # def clean_country_code(self):
    #     """
    #     Clean country code
    #     """
    #     country = self.data['country_code']
    #     country_code = CountryCode.objects.filter(country=country).first()
    #     return country_code

    def clean_phone_number(self):
        """
        Validate phone number entered by the user.
        """
        cleaned_data = self.cleaned_data
        phone_number = cleaned_data["phone_number"]
        # country = self.data['country_code']
        # country_code = CountryCode.objects.filter(country=country).first()
        return TwilioValidation().phone_validation(get_default(), phone_number)

    def save(self, commit=True):
        """
        Save user to the database.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

