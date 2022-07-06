from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE)


class User(AbstractUser):
    img = ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.username

