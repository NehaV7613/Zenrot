# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use the custom User model
        fields = ('username', 'email', 'password1', 'password2')  # Include fields you need
