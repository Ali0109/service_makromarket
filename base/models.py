import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_token(self, user_id):
        token, created = Token.objects.get_or_create(user_id=user_id)
        return token

    def create_user(self, username, password, **other_fields):
        if not username:
            raise ValueError("You must provide an username")

        user = self.model(username=username, **other_fields)
        user.set_password(password)
        user.save()

        self.create_token(user.id)
        return user

    def create_staff(self, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        return self.create_user(username, password, **other_fields)

    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **other_fields)

    def authenticate(self, username, password):
        if username and password:
            try:
                user = self.model.objects.get(
                    username=username, is_active=True
                )
                if not user.check_password(password, user.password):
                    return None
                else:
                    user.last_login = datetime.datetime.now()
                    user.save()
                    return user
            except User.DoesNotExist:
                return None
        else:
            return None


class User(AbstractUser):
    objects = UserManager()
