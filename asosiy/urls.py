from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BolimViewSet.as_view()),

    path('mahsulotlar/', MahsulotAPIView.as_view()),
    path('mahsulot/<int:pk>/', Bitta_MahsulotAPIView.as_view()),
    path('mahsulot/<int:pk>/izohlar/', Izoh_Mahsulot_APIView.as_view()),

    path('chegirmalilar/', ChegirmalilarAPIView.as_view()),

    path('izoh_ochir/<int:pk>/', IzohOchir.as_view()),

    ]
