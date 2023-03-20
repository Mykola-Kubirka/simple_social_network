from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import CustomUserCreateForm, CustomUserChangeForm
from users.models import User


class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreateForm

    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('name', )}),
        ('Important dates', {'fields': ('last_login', 'last_request')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')})
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2',)}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )

    list_display = ('id', 'email', 'is_admin', 'is_active')
    ordering = ('email', )
    list_filter = ()
    search_fields = ('email', )
    filter_horizontal = ()
    readonly_fields = ('last_login', 'last_request',)


admin.site.register(User, UserAdmin)
