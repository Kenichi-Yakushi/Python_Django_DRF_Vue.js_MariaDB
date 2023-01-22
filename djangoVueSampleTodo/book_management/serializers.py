from rest_framework import serializers
from book_management.models import Branch, Book, Category


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    """
    本一覧
    """
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        exclude = ('amount', 'isbn', 'created_at', 'updated_at')


class BookSerializer(serializers.ModelSerializer):
    """
    本
    """
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
