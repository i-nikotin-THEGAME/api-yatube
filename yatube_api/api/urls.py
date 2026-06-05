from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = "api"

# Создаём роутер для автоматической генерации URL-ов
router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"groups", GroupViewSet, basename="groups")
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comments")

urlpatterns = [
    path(f'{settings.API_VERSION}/', include(router.urls)),
    path(f'{settings.API_VERSION}/api-token-auth/', obtain_auth_token, name="api_token_auth"),
]
