from rest_framework import serializers
from .models import Books,Author

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields= '__all__'

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Author
        fields='__all__'
