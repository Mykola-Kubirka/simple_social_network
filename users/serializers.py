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


class UsersActivitySerializer(serializers.ModelSerializer):
    last_login = serializers.SerializerMethodField()
    last_request = serializers.SerializerMethodField()
    registration_date = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'registration_date', 'last_login', 'last_request')

    def get_registration_date(self, obj):
        return obj.registration_date.strftime('%H:%M, %d-%m-%Y')

    def get_last_login(self, obj):
        try:
            return obj.last_login.strftime('%H:%M, %d-%m-%Y')
        except AttributeError:
            return None

    def get_last_request(self, obj):
        try:
            return obj.last_request.strftime('%H:%M, %d-%m-%Y')
        except AttributeError:
            return None
