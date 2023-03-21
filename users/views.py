from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User
from users.serializers import UserRegistrationSerializer, UsersActivitySerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UsersActivityAPIView(generics.ListAPIView):
    serializer_class = UsersActivitySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.exclude(pk=self.request.user.pk)
