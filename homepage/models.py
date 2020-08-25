from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'age', 'homepage']
