from django import forms
from .models import Projects, Profile,Review,Comments
from django.core import validators


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude=['poster']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating','comment' ]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)

class UploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_name','project_photo','description','url','owner')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')