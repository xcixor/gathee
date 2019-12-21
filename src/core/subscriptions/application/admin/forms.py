"""Defines video forms."""
import os
import re
from django.forms import ModelForm, ValidationError
from django.core.files.images import get_image_dimensions
from subscriptions.models.video.video_models import PremiumVideo, DemoVideo
from subscriptions.models.course.course_models import Course
from subscriptions.models.company.company_models import Address
from subscriptions.utils.twilio import TwilioValidation
from subscriptions.models.auth.models import get_default


class VideoForm(ModelForm):
    class Meta:
        model = PremiumVideo
        fields = ["name", "video_file", "course", "description"]

    def clean_name(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        name = self.cleaned_data['name']
        if (regex.search(name) == None):
            return name
        else:
            raise ValidationError("Video name cannot contain special characters such as @# or !")

    def clean_video_file(self):
        video = self.cleaned_data['video_file']
        ext = os.path.splitext(video.name)[1]  # [0] returns path+filename
        valid_extensions = ['.flv', '.mp4', '.m3u8', '.ts', '.3gp', '.mov', '.avi', '.wmv', '.mkv']
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension. *{}*'.format(ext))
        else:
            return video

    def clean_description(self):
        description = self.cleaned_data['description']
        if not re.match(r'^[_\W]+$', description):
            return description
        else:
            raise ValidationError('Description cannot be special characters only')


class DemoVideoForm(ModelForm):
    class Meta:
        model = DemoVideo
        fields = ["name", "video_file"]

    def clean_name(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        name = self.cleaned_data['name']
        if (regex.search(name) == None):
            return name
        else:
            raise ValidationError("Video name cannot contain special characters such as @# or !")

    def clean_video_file(self):
        video = self.cleaned_data['video_file']
        ext = os.path.splitext(video.name)[1]  # [0] returns path+filename
        valid_extensions = ['.flv', '.mp4', '.m3u8', '.ts', '.3gp', '.mov', '.avi', '.wmv', '.mkv']
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension. *{}*'.format(ext))
        else:
            return video


class CoursesForm(ModelForm):

    class Meta:
        model = Course
        fields = ["title", "level", "description", "course_image", "price", "tutor"]

    def clean_title(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        title = self.cleaned_data['title']
        if (regex.search(title) == None):
            return title
        else:
            raise ValidationError("Video name cannot contain special characters such as @# or !")

    def clean_course_image(self):
        course_image = self.cleaned_data['course_image']
        if course_image:
            width, height = get_image_dimensions(course_image)
            if width < 260 or height < 165:
                raise ValidationError("The image cannot be less than 260px wide and 165px high")
            else:
                return course_image


class AddressForm(ModelForm):

    class Meta:
        model = Address
        fields = [
            "address_line_one",
            "address_line_two",
            "short_description",
            "email",
            "phone_number",
            "website"
            ]

    def clean_phone_number(self):
        """
        Validate phone number entered by the user.
        """
        cleaned_data = self.cleaned_data
        phone_number = cleaned_data["phone_number"]
        return TwilioValidation().phone_validation(get_default(), phone_number)
