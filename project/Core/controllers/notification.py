from datetime import datetime, timedelta

from django.conf import settings
from backend.accounts.app.models import User
from django.core.cache import cache
from typing import Any



class NotificationController:

    def __init__(self, user: User):
        self.user = user

    def add_notification(self, message: str, timeout: timedelta = settings.NOTIFICATION_TIMEOUT):
        now = datetime.now()
        self.user.notifications = [
            *self.user.notifications,
            {
                'message': message,
                'timeout': now + timeout,
            }
        ]
        self.user.save()
    
    def renew_notifications(self) -> list[dict]:
        now = datetime.now()
        active_notifications = [
            notification_obj for notification_obj in self.user.notifications
            if now > notification_obj['timeout']
        ]
        self.user.notifications = active_notifications
        self.user.save()
        return self.user.notifications
        


