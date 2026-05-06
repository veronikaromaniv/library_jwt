from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, RegisterSerializer, UserSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    # Використовуємо select_related для оптимізації запитів
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Ендпоінт для отримання інфо про себе
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Передаємо об'єкт request.user (залогінений юзер) у серіалізатор
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email
        })