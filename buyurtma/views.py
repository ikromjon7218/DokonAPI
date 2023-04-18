from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *
from asosiy.models import *

class BuyurtmalarAPIView(APIView):
    def get(self, request):
        hoz_profil = Profil.objects.get(user=request.user)
        queryset = Buyurtma.objects.filter(profil=hoz_profil)
        serializer = BuyurtmaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=Profil.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SavatItemAPIView(APIView):
    def get(self, request):
        savat = SavatItem.objects.filter(savat__profil__user=request.user)
        serializer = SavatItemSerializer(savat, many=True)
        return Response(serializer.data)

class TanlanganViewSet(ModelViewSet):
    queryset = Tanlangan.objects.all()
    serializer_class = TanlanganSerializer
