from rest_framework import serializers
from .models import Following

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ["id", "user", "book"]
        read_only_fields = ["id"]
