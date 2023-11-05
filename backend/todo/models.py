from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.mail import send_mail
from typing import Any
import uuid as uuid_lib


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self) -> str:
        return self.title


class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields) -> Any:
        email: str = self.normalize_email(email)
        user: Any = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields) -> Any:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        email: str = self.normalize_email(email)
        user: Any = self.model(email=email, **extra_fields)
        user.username = email
        user.set_password(password)
        user.save(using=self._db)
        return user


# custome user model class
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User"""

    class Meta:
        verbose_name: str = "CustomeUsers"
        verbose_name_plural: str = "CustomeUsers"

    id = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=30, unique=False)  # ユーザ氏名
    email = models.EmailField(unique=True, blank=True, null=True)  # メールアドレス = これで認証する

    is_active = models.BooleanField(default=True)  # アクティブ権限
    is_staff = models.BooleanField(default=True)  # スタッフ権限
    is_superuser = models.BooleanField(default=False)  # 管理者権限
    date_joined = models.DateTimeField(default=timezone.now)  # アカウント作成日時
    password_changed = models.BooleanField(default=False)  # パスワードを変更したかどうかのフラグ
    password_changed_date = models.DateTimeField(blank=True, null=True)  # 最終パスワード変更日時

    objects = UserManager()

    EMAIL_FIELD: str = "email"
    USERNAME_FIELD: str = "email"
    REQUIRED_FIELD: str = ""

    def clean(self) -> None:
        super().clean()
        self.email: Any = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs) -> None:
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self) -> str:
        return self.email

    def get_full_name(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username
