from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer, BookToCopySerializer
from django.core.validators import RegexValidator

class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    isbn = serializers.CharField(
        max_length=13,
        validators=[RegexValidator(r"^\d{13}$", "isbn must be a 13 characteres.")],
        required=True,
    )

    class Meta:
        model = Copy
        fields = [
            "id",
            "title",
            "author",
            "pages",
            "publishing_company",
            "isbn",
            "users",
            "is_loaned",
            "book",
        ]
        read_only_fields = ["id", "is_loaned"]


class CopyListSerializer(serializers.ModelSerializer):
    book = BookToCopySerializer(read_only=True)
    class Meta:
        model = Copy
        fields = [
            "id",
            "title",
            "author",
            "pages",
            "publishing_company",
            "isbn",
            "is_loaned",
            "book"
        ]
        
        read_only_fields = ["id", "is_loaned"]
