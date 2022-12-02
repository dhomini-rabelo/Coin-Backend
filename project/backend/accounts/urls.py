from django.urls import path
from . import api 

urlpatterns = [
    path('get-token', api.CustomTokenObtainPairView.as_view()),
    path('register', api.CreateUserAPI.as_view()),
    path('change-email', api.ChangeEmailAPI.as_view()),
    path('change-password', api.ChangePasswordAPI.as_view()),
    path('change-notification-time', api.ChangeNotificationTimeAPI.as_view()),
]
