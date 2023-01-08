import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.contrib.auth.models import UnicodeUsernameValidator

from phonenumber_field.modelfields import PhoneNumberField

from apis.base_models import BaseModel, UserLocation
from apis.users.managers import UserManager
from apis.users.utils.choices import ROLES


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username_validator = UnicodeUsernameValidator()

    email = models.CharField(
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator, validate_email],
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    phone_number = PhoneNumberField(unique=True, default=None, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    role = models.CharField(max_length=80, choices=ROLES, null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email_support = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def selected_address(self):
        customer_selected_address = self.user_addresses.filter(selected=True).first()
        if not customer_selected_address:
            return

        return customer_selected_address

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class UserDevice(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='device')
    device_id = models.CharField(max_length=200)


class CustomerAddress(BaseModel, UserLocation):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_addresses')
    house_no = models.CharField(max_length=50, null=True, blank=True)
    apartment_no = models.CharField(max_length=50, null=True, blank=True)
    street_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default=None, null=True, blank=True)
    label = models.CharField(max_length=30, null=True, blank=True)
    note_to_rider = models.TextField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        if self.house_no:
            return f"{self.house_no} {self.street_address} {self.city} {self.state}"

        if self.apartment_no:
            return f"{self.apartment_no} {self.street_address} {self.city} {self.state}"

        return f"{self.city} {self.state}"


class DeliveryAgent(BaseModel, UserLocation):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_agent')
    marked_location = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
