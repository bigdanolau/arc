from django.db import models
from django.contrib.auth.models import BaseUserManager


class  UserManager(BaseUserManager,models.Manager):

    def _create_user(self,username,password,email,nombre,empresa,is_staff,is_superuser,tipo,**extra_fields):
        user = self.model(
            username= username,
            email=email,
            nombre=email,
            empresa=empresa,
            is_staff = is_staff,
            is_superuser = is_superuser,
            tipo = tipo,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    
    def create_superuser(self,username,password=None,email=None,nombre=None,empresa=None,**extra_fields):
        return self._create_user(username,password,email,nombre,empresa,True,True,**extra_fields)
