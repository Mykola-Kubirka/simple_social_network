from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class CustomUserCreateForm(UserCreationForm):
    """
    Form represent create user in django admin
    """
    class Meta:
        model = User
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):
    """
    Form represent change user in django admin
    """
    class Meta:
        model = User
        fields = ('email',)
