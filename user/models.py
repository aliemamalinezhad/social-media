import os
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}', filename)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('is_staff'),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_('is_active'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Create Date'),
        default=timezone.now
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
