from typing import Any
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields: tuple = ("id", "title", "description", "completed")


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data) -> Any:
        raise NotImplementedError()

    def update(self, instance, validated_data) -> Any:
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data) -> Any:
        raise NotImplementedError()

    def update(self, instance, validated_data) -> Any:
        raise NotImplementedError()
