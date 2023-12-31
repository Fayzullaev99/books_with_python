from django.shortcuts import render
from rest_framework.generics import ListAPIView
from books.models import Books
from .serializers import BookSerializer

# Create your views here.

class BookApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

