from django.contrib import admin
from django.urls import path, include
from todo.views import TodoApiView, TodoDetailApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", TodoApiView.as_view()),
    path("api/<int:todo_id>/", TodoDetailApiView.as_view()),
]
