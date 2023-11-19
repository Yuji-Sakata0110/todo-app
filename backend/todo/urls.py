from django.urls import path, URLResolver
from .views import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
    TodoApiView,
    TodoDetailApiView,
    SignupView,
    LoginView,
    LogoutView,
)

urlpatterns: list[URLResolver] = [
    path(
        "auth/token/", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "auth/token/refresh/", DecoratedTokenRefreshView.as_view(), name="token_refresh"
    ),
    path("auth/signup/", SignupView.as_view(), name="auth_sign_up"),
    path("auth/login/", LoginView.as_view(), name="auth_login"),
    path("auth/logout/", LogoutView.as_view(), name="auth_lognout"),
    path("todos/", TodoApiView.as_view(), name="todo-list-create"),
    path("todos/<int:pk>/", TodoDetailApiView.as_view(), name="todo-detail"),
]
