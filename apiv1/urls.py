from django.urls import path, include
from rest_framework import routers

from .views import ArticleViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls))
]