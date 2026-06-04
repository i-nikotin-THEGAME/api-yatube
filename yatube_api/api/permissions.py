from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение: автор может редактировать/удалять свой объект,
    остальным доступ только на чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем GET, HEAD, OPTIONS запросы любому аутентифицированному пользователю
        if request.method in permissions.SAFE_METHODS:
            return True

        # Запись разрешена только автору
        return obj.author == request.user
