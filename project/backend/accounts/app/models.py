from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE)
from backend.accounts.app.support.models.choices import NOTIFICATION_TIME_CHOICES



class User(AbstractUser):
    notification_time = CharField(max_length=64, choices=NOTIFICATION_TIME_CHOICES, default=NOTIFICATION_TIME_CHOICES[0][0])

    def __str__(self):
        return self.username

