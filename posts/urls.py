from django.urls import path, include
from rest_framework.routers import SimpleRouter

from posts.views import UserPostViewSet

router = SimpleRouter()

router.register('', UserPostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', TokenObtainPairView.as_view(), name='login-token'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
