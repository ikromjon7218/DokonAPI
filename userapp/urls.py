from django.contrib import admin
from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('create/', UserCreateAPI.as_view()),
    path('profil/', ProfilViewSet.as_view()),

    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
]