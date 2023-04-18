from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BuyurtmaAPIView.as_view()),
    path('savat/', SavatItemAPIView.as_view()),


    ]