"""Contains forms associated with the contact page."""
from subscriptions.utils.email import send_email
from django import forms
from subscriptions.utils.validations import clean_value


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    name = forms.CharField(max_length=80)


    def clean_name(self):
        """
        Validate name entered by the user.
        """
        name = self.cleaned_data["name"]
        return clean_value(name, "Name")

    def clean_message(self):
        """
        Validate name entered by the user.
        """
        message = self.cleaned_data["message"]
        return clean_value(message, "Message")

    def clean_subject(self):
        """
        Validate name entered by the user.
        """
        subject = self.cleaned_data["subject"]
        return clean_value(subject, "Subject")

    def clean_email(self):
        return self.cleaned_data['email']


    def send_email(self):
        """Send user message to company."""
        send_email(
            self.clean_subject(),
            self.clean_email(),
            'ndunguwanyinge@gmail.com',
            self.clean_message()
            )
