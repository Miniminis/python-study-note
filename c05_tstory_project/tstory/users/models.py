from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Femail'),
    ('N', 'Not to disclose'),
]

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, username, gender, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must set TRUE in "is_staff" field ')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must set TRUE in "is_sueruser" field ')

        return self._create_user(email, '', password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(verbose_name='username', max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default='N')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

