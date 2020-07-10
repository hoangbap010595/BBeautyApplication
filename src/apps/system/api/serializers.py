from rest_framework import serializers
from django.contrib.auth.models import User
from apps.account.models import Profile, Setting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['id', 'is_enable_notification']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'image_url']


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(many=False, read_only=True)
    setting = SettingSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'setting']
