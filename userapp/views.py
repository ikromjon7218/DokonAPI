from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *
from buyurtma.models import *
from .serializers import *

class UserCreateAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.data['username'],
                password=serializer.data['password'] )
            if user is None:
                return Response({"xabar": "Bunaqa user yo'q"}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({"xabar": "Tizimga kirildi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({"xabar": "User tizimdan chiqarildi."}, status=status.HTTP_200_OK)

class ProfilViewSet(ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Savat.objects.create(profil=Profil.objects.last())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
