from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserRegistrationAPIView, UsersActivityAPIView

urlpatterns = [
    path('users/sign-up/', UserRegistrationAPIView.as_view(), name='sign-up'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login-token'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('users/activity/', UsersActivityAPIView.as_view(), name='users_activity')
]
