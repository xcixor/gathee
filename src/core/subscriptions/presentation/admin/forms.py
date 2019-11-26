"""Defines video forms."""
import os
import re
from django.forms import ModelForm, ValidationError
from subscriptions.models.video.models import Video


class VideoForm(ModelForm):
    class Meta:
        model=Video
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
        from django.core.exceptions import ValidationError
        ext = os.path.splitext(video.name)[1]  # [0] returns path+filename
        valid_extensions = ['.flv', '.mp4', '.m3u8', '.ts', '.3gp', '.mov', '.avi', '.wmv']
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension. *{}*'.format(ext))
        else:
            return video