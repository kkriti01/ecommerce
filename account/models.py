from __future__ import unicode_literals

from django.contrib.auth .models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def Create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError("users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )

        user.set_password(password)
        user.save(self._db)
        return user

    def Create_superuser(self, email, date_of_birth, password):
        """
        Create super user with given email ,date of birth and given password
        """
        user = self.create_user(email, password=password, date_of_birth=date_of_birth)
        user.is_admin = True
        user.save(self._db)
        return user


class Myuser(AbstractUser):
    """
    Custom user
    """
    role_choices = (
        ('admin', 'Administrator'),
        ('user', 'user')
    )
    role = models.CharField(max_length=7, choices=role_choices)
    mobile = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modifiedby = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def is_Admin(self):
        return True if self.role == 'admin' else False

    def is_user(self):
        return True if self.role == 'user' else False
