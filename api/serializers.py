from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = Profile
        fields = (
            'username', 'email', 'phone',
            'first_name', 'last_name', 'patronymic',
            'gender', 'birth_date'
        )
        depth = 1