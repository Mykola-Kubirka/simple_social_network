from django.contrib import admin

from posts.models import Post, PostLike


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'body', 'create_date']
    fieldsets = (
        (None, {'fields': ('user', 'title', 'body')}),
        ('Important dates', {'fields': ('create_date',)})
    )
    readonly_fields = ('create_date',)


class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'create_date']
    fieldsets = (
        (None, {'fields': ('user', 'post')}),
        ('Important dates', {'fields': ('create_date',)})
    )
    readonly_fields = ('create_date',)


admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
