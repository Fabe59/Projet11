from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    """Form to create the user register account,
    based on the Django User model."""

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
