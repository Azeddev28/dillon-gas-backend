import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from apis.base_models import TimeStamp
from apis.users.managers import UserManager


class User(AbstractBaseUser, TimeStamp, PermissionsMixin):
    ROLES = (
        ('delivery_agent', 'delivery_agent'),
        ('owner', 'owner'),
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    role = models.CharField(max_length=80, choices=ROLES)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

