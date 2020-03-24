from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_name', 'project_photo', 'description', 'project_link', 'url',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo', 'user_id')