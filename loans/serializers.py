from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer
from copies.serializers import CopyListSerializer

class LoansBooksSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

    user = UserSerializer(read_only=True)
    copy = CopyListSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = [
            "id",
            "date_collected",
            "date_limit_return",
            "date_returned",
            "user",
            "copy",
        ]
        read_only_fields = [
            "id",
            "date_collected",
            "date_limit_return",
            "date_returned",
            "user",
            "copy",
        ]
