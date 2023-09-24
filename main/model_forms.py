from django.forms import ModelForm
from .models import Profile


class UserProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "email")
