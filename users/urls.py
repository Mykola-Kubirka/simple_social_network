from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from authentication.views import SignUpView, ActivateUserView, RequestPasswordResetView, ResetPasswordView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='obtain-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    # path('sign-up/', SignUpView.as_view(), name='sign-up'),
]
