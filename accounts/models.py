import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

# Create your models here.

class ORMUser(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), max_length=64, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'residence_state']

    objects = UserManager()

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=False, unique=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False, unique=False)
    residence_state = models.CharField(_('residence state'), max_length=20, blank=False)
    jwt_secret = models.UUIDField(_('JWT user specific secret'), default=uuid.uuid4)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

def jwt_get_secret_key(user_id):
    return ORMUser.objects.get(user_id=user_id).jwt_secret