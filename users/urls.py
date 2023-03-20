from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserRegistrationAPIView

urlpatterns = [
    path('sign-up/', UserRegistrationAPIView.as_view(), name='sign-up'),
    path('login/', TokenObtainPairView.as_view(), name='login-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
