import datetime

from django.utils import timezone
from rest_framework import serializers


class AnalyticsDateSerializer(serializers.Serializer):
    date_from = serializers.DateTimeField(default=timezone.now()-datetime.timedelta(days=7))
    date_to = serializers.DateTimeField(default=timezone.now())
