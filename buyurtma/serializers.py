from rest_framework import serializers
from .models import *
# from django.core.validators import MinValueValidator
# from django.db.models import Avg
class TanlanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanlangan
        fields = '__all__'

class SavatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = '__all__'

class SavatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavatItem
        fields = '__all__'
    def to_representation(self, instance):
        malumot = super().to_representation(instance)
        narx = instance.mahsulot.narx - (instance.mahsulot.chegirma * instance.mahsulot.narx / 100)
        malumot["umumiy_summa"] = narx * instance.miqdor
        return malumot
class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'