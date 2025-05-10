from rest_framework import serializers
from Home.models import UserRegistration


class UserRegistrationSerializer(serializers.Serializer):
    class Meta:
        model=UserRegistration
        fields='__all__'
