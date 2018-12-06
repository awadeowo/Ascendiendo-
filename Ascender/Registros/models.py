from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator

# Create your models here.

class CustomUserManager(UserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Usuario debe ingresar su Email")

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            password=password,
            username=username,
            email=email,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    id_user = models.AutoField(max_length=5, primary_key=True)
    email = models.EmailField(max_length=30, unique=True, verbose_name='Direccion de correo')  #obtener email con get_email_field_name()
    username = models.CharField(max_length=40, unique=False, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, misPerris):
        return True

    @property
    def is_staff(self):
        return self.is_admin
