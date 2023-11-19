from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import HttpRequest
from django.db.models.manager import BaseManager
from django.contrib.auth.models import AbstractBaseUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, Token
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.middleware import csrf
from .models import Todo, User
from .serializers import (
    TodoSerializer,
    SignupSerializer,
    LoginSerializer,
)
from drf_yasg.utils import swagger_auto_schema


class SignupView(APIView):
    """AccessTokenを返却する。FrontendのLocalStrageに保存する。"""

    def post(self, request: HttpRequest) -> Response:
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user: User | None = User.objects.filter(email=email).first()
            if user is None:
                try:
                    new_user = User.objects.create_user(email, password)
                    login(request, new_user)
                    refresh: Token = RefreshToken.for_user(new_user)
                    access_token = str(refresh.access_token)
                    return Response({"access_token": access_token}, status=HTTP_200_OK)
                except Exception as e:
                    raise f"Communication Error: {new_user=} {e}"

            else:
                return Response(
                    {"UnAuthorized Error": "This requested user has already existed."},
                    status=HTTP_401_UNAUTHORIZED,
                )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """AccessTokenを返却する。FrontendのCookieに保存する。"""

    def post(self, request: HttpRequest) -> Response:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user: AbstractBaseUser | None = authenticate(
                request, email=email, password=password
            )
            if user is not None:
                if user.is_active:
                    refresh: Token = RefreshToken.for_user(user)
                    response = Response()
                    response.set_cookie(
                        key="access_token",
                        value=str(refresh.access_token),
                        expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                    )
                    # response.set_cookie(
                    #     key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                    #     value=str(refresh.access_token),
                    #     expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                    #     secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    #     httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                    #     samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                    # )
                    csrf.get_token(request)
                    try:
                        login(request, user)
                        response.data = {"login_status": request.user.is_authenticated}
                        response.status_code = HTTP_200_OK
                        return response
                    except Exception as e:
                        raise Response(
                            {"Communication Error": e},
                            status=HTTP_500_INTERNAL_SERVER_ERROR,
                        )
            else:
                return Response(status=HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """SignoutするClassView"""

    def post(self, request: HttpRequest) -> Response:
        logout(request)
        return Response({}, status=HTTP_200_OK)


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(responses={HTTP_200_OK: TokenObtainPairSerializer})
    def post(self, request, *args, **kwargs) -> Response:
        response: Response = super().post(request, *args, **kwargs)
        access_token = response.data.get("access")
        refresh_token = response.data.get("refresh")

        response.set_cookie(key="access_token", value=access_token, httponly=True)
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)

        return response


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(responses={HTTP_200_OK: TokenObtainPairSerializer})
    def post(self, request, *args, **kwargs) -> Response:
        response: Response = super().post(request, *args, **kwargs)
        access_token = response.data.get("access")
        refresh_token = response.data.get("refresh")

        response.set_cookie(key="access_token", value=access_token, httponly=True)
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)

        return response


class TodoApiView(ListCreateAPIView):
    queryset: BaseManager[Todo] = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request: HttpRequest) -> Response:
        print(request.COOKIES)
        if not request.user.is_authenticated:
            return Response({"message": "Unauthorized."}, status=HTTP_401_UNAUTHORIZED)

        return Response(request.user.is_authenticated, status=HTTP_200_OK)


class TodoDetailApiView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    # add permission to check if user is authenticated
    # permission_classes: list[type[IsAuthenticated]] = [IsAuthenticated]
    queryset: BaseManager[Todo] = Todo.objects.all()
    serializer_class = TodoSerializer
