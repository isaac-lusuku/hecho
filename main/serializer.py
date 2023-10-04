from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class SubtaskSerializer(ModelSerializer):
    class Meta:
        model = Subtask
        fields = "__all__"


class ReviewsSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Reviews
        fields = ["user", "review"]