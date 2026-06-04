from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post, Comment
from .serializers import GroupSerializer, PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для постов: чтение, создание, редактирование, удаление"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        # При создании поста автоматически подставляем автора
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для групп: только чтение"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для комментариев: чтение, создание, редактирование, удаление"""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def get_queryset(self):
        # Фильтруем комментарии по post_id из URL
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        # При создании комментария подставляем автора и пост
        post_id = self.kwargs.get("post_id")
        serializer.save(author=self.request.user, post_id=post_id)
