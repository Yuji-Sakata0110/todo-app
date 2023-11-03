from django.contrib import admin
from django.urls import path, URLResolver
from todo.views import TodoApiView, TodoDetailApiView, auth_login

urlpatterns: list[URLResolver] = [
    path("admin/", admin.site.urls),
    path("auth/login/", auth_login, name="auth_login"),
    path("api/", TodoApiView.as_view()),
    path("api/<int:todo_id>/", TodoDetailApiView.as_view()),
]
