from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
# class Model User personaliser

class UserManager(BaseUserManager):

    def _create_user(self, username,password,email, first_name, last_name, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('Users must have an username ')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None,password=None, email=None, first_name=None, last_name=None, **extra_fields):
        return self._create_user(username, password,email, first_name, last_name, False, False, **extra_fields)

    def create_superuser(self, username, email,password, first_name, last_name, **extra_fields):
        user = self._create_user(username, password,email,first_name,last_name, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    SEXE = (
        ("F", "FEMININ"),
        ("M", "MASCULIN")
    )


    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    birthday = models.DateField(max_length=254, null=True, blank=True)
    sexe = models.CharField(choices=SEXE, default="M", null=True, blank=True, max_length=10)
    phone = models.CharField(max_length=10, null=True, blank=True)
    adresse = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_email(self):
        return self.email
