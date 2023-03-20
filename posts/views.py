from rest_framework import viewsets

from posts.models import Post
from posts.serializers import UserPostSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserPostSerializer
