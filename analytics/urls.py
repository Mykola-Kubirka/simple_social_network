from django.urls import path

from analytics.views import LikeAnalyticsAPIView

urlpatterns = [
    path('', LikeAnalyticsAPIView.as_view(), name='like_analytics'),
]
