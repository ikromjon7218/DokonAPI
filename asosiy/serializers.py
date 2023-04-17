from rest_framework import serializers
from .models import *
from django.core.validators import MinValueValidator
from django.db.models import Avg
class BolimSerializer(serializers.ModelSerializer):
    # bolimlar = BolimSerializer(many=True)
    class Meta:
        model = Bolim
        fields = '__all__'

class MahsulotSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=15)
    narx = serializers.IntegerField()
    chegirma = serializers.IntegerField()
    brend = serializers.CharField(max_length=15)
    batafsil = serializers.CharField(max_length=200)
    rasm = serializers.FileField(allow_empty_file=True, use_url=True)
    bolim = serializers.PrimaryKeyRelatedField(queryset=Bolim.objects.all())
    holat = serializers.CharField(max_length=20)
    mavjud = serializers.BooleanField(default=True)
    sotuvchi = serializers.PrimaryKeyRelatedField(queryset=Profil.objects.all(), required=False)

    def to_representation(self, instance):
        malumot = super().to_representation(instance)
        malumot['yangi_narx'] = instance.chegirma*instance.narx/100
        o = Izoh.objects.filter(mahsulot=instance)
        malumot['ortacha_baho'] = o.aggregate(Avg('reyting'))['reyting__avg']
        return malumot
    def validate_chegirma(self, qiymat):
        if qiymat < 0 or qiymat > 50:
            raise serializers.ValidationError("Chegirma 0 dan kichik yoki 50 dan baland foizda bo'lishi mumkin emas")
        return qiymat

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'

    def validate_reyting(self, qiymat):
        if qiymat < 1 or qiymat > 5:
            raise serializers.ValidationError("Noto'g'ri reyting bal kiritildi")
        return qiymat
