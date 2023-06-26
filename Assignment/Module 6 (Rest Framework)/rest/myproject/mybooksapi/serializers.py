from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=50)
    isbn = serializers.CharField(max_length=50)
    publisher = serializers.CharField(max_length=100)
