import os
import uuid
from django.utils.translation import gettext as _
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from utils.base_errors import BaseErrors
from utils import GeneralModel


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}', filename)


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user


class User(AbstractBaseUser, GeneralModel):
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=200,
        unique=True,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        max_length=300,
        unique=True,

    )

    follow = models.ManyToManyField(
        'user.User',
        verbose_name=_('Follow'),
    )
    follower_count = models.PositiveIntegerField(
        verbose_name=_('Total Follower'),
        default=0,
    )
    following_count = models.PositiveIntegerField(
        verbose_name=_('Total Following'),
        default=0,
    )
    post_count = models.PositiveIntegerField(
        verbose_name=_('Total post'),
        default=0,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

