from django.urls import path
from . import api 

urlpatterns = [
    path('register', api.CreateUserAPI.as_view()),
    path('change-email', api.ChangeEmailAPI.as_view()),
    path('change-password', api.ChangePasswordAPI.as_view()),
]
