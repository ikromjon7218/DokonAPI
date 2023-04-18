from django.contrib import admin
from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', UserCreate.as_view()),
    path('user_create/', UserCreate.as_view()),
    path('login/', LoginAPIView.as_view()),
]