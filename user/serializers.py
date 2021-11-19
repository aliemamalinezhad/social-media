from pyexpat import model

from django.contrib.auth import get_user_model
from django.utils.timezone import now, __all__
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = __all__

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
