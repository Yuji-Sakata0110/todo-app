from django.urls import path, URLResolver
from .views import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
    TodoApiView,
    TodoDetailApiView,
)

urlpatterns: list[URLResolver] = [
    path("token/", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", DecoratedTokenRefreshView.as_view(), name="token_refresh"),
    path("todos/", TodoApiView.as_view(), name="todo-list-create"),
    path("todos/<int:pk>/", TodoDetailApiView.as_view(), name="todo-detail"),
]
