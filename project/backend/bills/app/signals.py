from Core.controllers.cache import bill_cache
from .models import Bill
from django.db.models.signals import post_save, post_delete


def renew_bill_cache(sender, instance, created, **kwargs):
    bill_cache.delete_all()


post_save.connect(renew_bill_cache, sender=Bill)
post_delete.connect(renew_bill_cache, sender=Bill)