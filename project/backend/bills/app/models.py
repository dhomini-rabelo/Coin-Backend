from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SET_NULL, CASCADE)
from backend.accounts.app.models import User
from backend.bills.app.support.choices import BILL_TYPE_CHOICES, PAYMENT_METHOD_CHOICES


class Bill(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=256)
    description = TextField(default='', blank=True)
    bill_type = CharField(max_length=256, choices=BILL_TYPE_CHOICES)
    value = DecimalField(max_digits=50, decimal_places=2)
    payment_method = CharField(max_length=256, choices=PAYMENT_METHOD_CHOICES)
    day = PositiveIntegerField(null=True)
    partials = PositiveIntegerField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    

    def save(self, *args, **kwargs):
        if self.day and (int(self.day) > 28):
            raise Exception('Invalid day for save notification')
        else:
            return super().save(*args, **kwargs)

