from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, **extra_fields)

class User(AbstractUser):

    username      = None
    email         = None
    chipID        = models.IntegerField(_("chip ID"),unique=True)
    studentID     = models.IntegerField(_("student ID"))
    expression    = models.CharField(_("expression"), max_length=100,blank=True,null=True)
    solution      = models.IntegerField(_("solution"),blank=True,null=True)
    exp_timestamp = models.IntegerField(_("expression timestamp"),blank=True,null=True)
    created       = models.DateTimeField(_("Created"), auto_now_add=True)
    updated       = models.DateTimeField(_("Created"), auto_now=True)

    USERNAME_FIELD = 'chipID'
    REQUIRED_FIELDS = ['studentID']
    objects = UserManager()

    # class Meta:
    #     unique_together = ['chipID','studentID']

    def __str__(self) -> str:
        return str(self.first_name) + ' ' + str(self.last_name) + ' (' + str(self.studentID) + ')'