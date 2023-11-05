import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.db.models.manager import BaseManager
from django.contrib.auth.models import AbstractBaseUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from drf_yasg.utils import swagger_auto_schema


def auth_login(request) -> HttpResponse:
    body: dict = json.loads(request.body.decode("utf-8"))
    username: str = body.get("username")
    password: str = body.get("password")

    user: AbstractBaseUser | None = authenticate(
        request, username=username, password=password
    )

    if user is not None:
        login(request, user)
        return HttpResponse(user, status=HTTP_200_OK)
    else:
        raise Exception("except")


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(responses={HTTP_200_OK: TokenObtainPairSerializer})
    def post(self, request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(responses={HTTP_200_OK: TokenObtainPairSerializer})
    def post(self, request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


# api views
class TodoApiView(ListCreateAPIView):
    # add permission to check if user is authenticated
    # permission_classes: list[type[IsAuthenticated]] = [IsAuthenticated]
    queryset: BaseManager[Todo] = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailApiView(RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    # permission_classes: list[type[IsAuthenticated]] = [IsAuthenticated]
    queryset: BaseManager[Todo] = Todo.objects.all()
    serializer_class = TodoSerializer
