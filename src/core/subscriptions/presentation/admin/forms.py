"""Defines video forms."""
import os
import re
from django.forms import ModelForm, ValidationError
from django.core.files.images import get_image_dimensions
from subscriptions.models.video.models import PremiumVideo, DemoVideo
from subscriptions.models.courses.models import Course


class VideoForm(ModelForm):
    class Meta:
        model = PremiumVideo
        fields = ["name", "video_file", "course"]

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
        valid_extensions = ['.flv', '.mp4', '.m3u8', '.ts', '.3gp', '.mov', '.avi', '.wmv']
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension. *{}*'.format(ext))
        else:
            return video


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
        valid_extensions = ['.flv', '.mp4', '.m3u8', '.ts', '.3gp', '.mov', '.avi', '.wmv']
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension. *{}*'.format(ext))
        else:
            return video


class CoursesForm(ModelForm):

    class Meta:
        model = Course
        fields = ["title", "description", "course_image"]

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
