from rest_framework import serializers

from posts.models import Post


class UserPostSerializer(serializers.ModelSerializer):
    create_date = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('pk', 'user', 'title', 'body', 'create_date', 'likes')

    def to_internal_value(self, data):
        data['user'] = self.context.get('request').user.pk
        return super().to_internal_value(data)

    def get_create_date(self, obj):
        return obj.create_date.strftime('%d-%m-%Y')

    def get_likes(self, obj):
        return obj.likes.count()
