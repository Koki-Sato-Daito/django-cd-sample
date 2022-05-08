from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer, ArticleSerializer
from .models import Article


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
