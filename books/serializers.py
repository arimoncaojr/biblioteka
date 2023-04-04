from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "pages", "publishing_company"]
        read_only_fields = ["id"]


class BookToCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id"]
