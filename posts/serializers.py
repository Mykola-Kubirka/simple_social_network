from rest_framework import serializers

from posts.models import Post


class UserPostSerializer(serializers.ModelSerializer):
    create_date = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('pk', 'user', 'title', 'body', 'create_date', 'likes', 'is_liked')

    def to_internal_value(self, data):
        data['user'] = self.context.get('request').user.pk
        return super().to_internal_value(data)

    def get_create_date(self, obj):
        return obj.create_date.strftime('%d-%m-%Y')

    def get_likes(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        return obj.likes.filter(user=self.context.get('request').user).exists()
