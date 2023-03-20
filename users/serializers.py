from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirmation_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'confirmation_password')

    def validate_email(self, value):
        return value.lower()

    def validate(self, data):
        if data['password'] != data['confirmation_password']:
            raise serializers.ValidationError("Passwords fields didn't match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )

        return user
