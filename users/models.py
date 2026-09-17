import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class UserManager(BaseUserManager):

    def create_user(
        self,
        email,
        full_name,
        dob,
        phone_number=None,
        password=None,
        **extra_fields
    ):
        if not email:
            raise ValueError("Email is required.")

        if not full_name:
            raise ValueError("Full name is required.")

        if not dob:
            raise ValueError("Date of birth is required.")

        if not password:
            raise ValueError("Password is required.")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            full_name=full_name,
            dob=dob,
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email,
        full_name,
        dob=None,
        phone_number=None,
        password=None,
        **extra_fields
    ):
        if not dob:
            raise ValueError("Date of birth is required.")

        user = self.create_user(
            email=email,
            full_name=full_name,
            dob=dob,
            phone_number=phone_number,
            password=password,
            user_type=User.ADMIN,
            **extra_fields
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)

        return user
def create_superuser(
    self,
    email,
    full_name,
    dob=None,
    phone_number=None,
    password=None,
    **extra_fields
):
    if not dob:
        raise ValueError("Date of birth is required.")

    user = self.create_user(
        email=email,
        full_name=full_name,
        dob=dob,
        phone_number=phone_number,
        password=password,
        user_type=User.ADMIN,
        **extra_fields
    )

    user.is_staff = True
    user.is_superuser = True
    user.is_active = True

    user.save(using=self._db)

    return user

class User(AbstractBaseUser, PermissionsMixin):

    ADMIN = "SUPER ADMIN"
    STAFF = "STAFF"

    USER_TYPE_CHOICE = (
        (ADMIN, "Super Admin"),
        (STAFF, "Staff"),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    full_name = models.CharField(
        _("full name"),
        max_length=100
    )

    email = models.EmailField(
        _("email address"),
        unique=True
    )

    dob = models.DateField(
        _("date of birth")
    )

    phone_number = models.CharField(
        _("phone number"),
        max_length=10,
        unique=True,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(10)
        ]
    )

    user_type = models.CharField(
        _("user type"),
        max_length=50,
        choices=USER_TYPE_CHOICE,
        default=STAFF
    )

    is_active = models.BooleanField(
        _("is active"),
        default=True
    )

    is_staff = models.BooleanField(
        _("is staff"),
        default=False
    )

    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["full_name","dob"]

    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return self.full_name


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    full_name = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        max_length=255,
        unique=True
    )

    phone_number = models.CharField(
        max_length=20
    )

    dob = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.email

    