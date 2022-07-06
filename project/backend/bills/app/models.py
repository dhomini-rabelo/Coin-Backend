from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE)
from backend.accounts.app.models import User


class Bill(Model):

    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=256)
    description = TextField()
    bill_type = CharField(max_length=256)
    value = DecimalField(max_digits=50, decimal_places=2)
    is_income = BooleanField()
    use_notification = BooleanField(default=False, blank=True)
    date = DateField(blank=True, null=True)
    