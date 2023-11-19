from django.contrib import admin
from django.urls import path, URLResolver, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 認証認可が通らなければ、swaggerには入れないようにする。
schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version="v3",
        description="Todo API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns: list[URLResolver] = [
    path("admin/", admin.site.urls),
    path("api/", include("todo.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
