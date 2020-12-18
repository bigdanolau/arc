from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = [
        ('C',"Condominio"),
        ('A',"administrador")
    ]
    username = models.CharField( max_length=30,unique= True)
    email = models.EmailField()
    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10 ,choices=GENDER_CHOICES)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre','empresa','tipo']
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombre + ' ' + self.empresa
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
