from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from posts.models import Post, PostLike
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import UserPostSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserPostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly | IsAdminUser]

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, *args, **kwargs):
        like_obj, created = PostLike.objects.get_or_create(
            post=self.get_object(), user=self.request.user
        )
        # like post
        if created:
            return Response(status=status.HTTP_201_CREATED)
        # unlike post
        like_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
