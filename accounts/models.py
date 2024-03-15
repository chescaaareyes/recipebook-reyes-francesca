from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500, validators=[MinLengthValidator(255)])
