from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Todo, User


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list: tuple[str] = ("title", "description", "completed")


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets: tuple = (
        (None, {"fields": ("username", "password")}),
        (
            _(
                "Personal Info",
            ),
            {"fields": ("email",)},
        ),
        (
            _(
                "Permissions",
            ),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _(
                "Password",
            ),
            {
                "fields": (
                    "password_changed",
                    "password_changed_date",
                )
            },
        ),
        (
            _(
                "Important Dates",
            ),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

    list_display: tuple[str] = (
        "username",
        "email",
        "is_active",
    )
