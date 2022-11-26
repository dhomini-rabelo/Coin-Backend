from django.urls import path
from . import views, api 

urlpatterns = [
    path('register', api.CreateUserApi.as_view()),
]
