import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .serializers import TodoSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo


def auth_login(request) -> HttpResponse:
    body: dict = json.loads(request.body.decode("utf-8"))
    username: str = body.get("username")
    password: str = body.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse(user, status=HTTP_200_OK)
    else:
        raise Exception("except")


# api views
class TodoApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes: list[type[IsAuthenticated]] = [IsAuthenticated]

    # 1 get method show all todos
    def get(self, request, *args, **kwargs) -> Response:
        """
        List all the todo items for given requested user
        """
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs) -> Response:
        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "completed": request.data.get("completed"),
            "user": request.user.id,
        }
        serializer = TodoSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        # invalid error
        return Response(
            {"res": "Request is invalid."},
            status=HTTP_400_BAD_REQUEST,
        )


class TodoDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes: list[type[IsAuthenticated]] = [IsAuthenticated]

    def get_object(self, todo_id, user_id) -> Todo | None:
        """
        Helper method to get the object with given todo_id, and user_id
        """
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None

    # 1. get method Retrieve detail data
    def get(self, request, todo_id, *args, **kwargs) -> Response:
        """
        Retrieves the Todo with given todo_id
        """
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=HTTP_400_BAD_REQUEST,
            )

        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=HTTP_200_OK)

    # 2. Update
    def put(self, request, todo_id, *args, **kwargs) -> Response:
        """
        Updates the todo item with given todo_id if exists
        """
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=HTTP_400_BAD_REQUEST,
            )
        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "completed": request.data.get("completed"),
            "user": request.user.id,
        }
        serializer = TodoSerializer(instance=todo_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, todo_id, *args, **kwargs) -> Response:
        """
        Deletes the todo item with given todo_id if exists
        """
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=HTTP_400_BAD_REQUEST,
            )
        todo_instance.delete()
        return Response({"res": "Object deleted!"}, status=HTTP_200_OK)
