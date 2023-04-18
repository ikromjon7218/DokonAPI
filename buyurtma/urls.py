from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BuyurtmalarAPIView.as_view()),
    path('savat/', SavatItemAPIView.as_view()),


    ]