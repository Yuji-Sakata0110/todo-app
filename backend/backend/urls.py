from django.contrib import admin
from django.urls import path, URLResolver, include
from todo.views import TodoApiView, TodoDetailApiView, auth_login

urlpatterns: list[URLResolver] = [
    path("admin/", admin.site.urls),
    path("api/", include("todo.urls")),
]
