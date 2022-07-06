from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE)


class User(AbstractUser):

    def __str__(self):
        return self.username

