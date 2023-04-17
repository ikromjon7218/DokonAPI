from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

class BolimViewSet(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer

class MahsulotAPIView(APIView):
    def get(self, request):
        search = request.query_params.get('search', None)
        queryset = Mahsulot.objects.all()
        if search:
            queryset = queryset.filter(nom__icontains=search)
        serializer = MahsulotSerializer(queryset, many=True)
        return Response(serializer.data)

class Bitta_MahsulotAPIView(APIView):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        serializer = MahsulotSerializer(mahsulot)
        return Response(serializer.data)
class ChegirmalarAPIView(APIView):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.order_by('-chegirma')
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)



class Izoh_Mahsulot_APIView(APIView):
    def get(self, request, pk):
        izohlar = Izoh.objects.filter(mahsulot__id=pk)
        serializer = IzohSerializer(izohlar, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        izoh = request.data
        serializer = IzohSerializer(data=izoh)
        if serializer.is_valid():
            serializer.save(mahsulot =  Mahsulot.objects.get(id=pk), profil = Profil.objects.get(user=request.user))

            natija = serializer.data
            natija['mahsulot'] = pk
            natija['profil'] = Profil.objects.get(user=request.user).id
            print(request.user, natija)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IzohOchir(APIView):
    def delete(self, request, pk):
        Izoh.objects.get(id=pk).delete()
        return Response({"success": "True"}, status=status.HTTP_200_OK)

