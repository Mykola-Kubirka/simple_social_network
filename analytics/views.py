from django.db.models import Count
from django.db.models.functions import TruncDate
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics.serializers import AnalyticsDateSerializer
from posts.models import PostLike


class LikeAnalyticsAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        analytic_serializer = AnalyticsDateSerializer(data=request.query_params)
        analytic_serializer.is_valid(raise_exception=True)

        analytic_likes = PostLike.objects.filter(
            create_date__gte=analytic_serializer.data['date_from'],
            create_date__lt=analytic_serializer.data['date_to']
        ).values(
            date=TruncDate('create_date__date')
        ).annotate(
            count_likes=Count('pk')
        ).order_by('date')

        return Response(analytic_likes)
