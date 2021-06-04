from rest_framework import serializers
from .models import createUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = createUser
        fields = ['id', 'fullname', 'mailid', 'phoneNumber']
    