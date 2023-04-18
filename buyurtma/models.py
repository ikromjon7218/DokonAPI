from django.db import models
from asosiy.models import *
from django.db.models import Sum

class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.profil}"

class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.profil}"

class SavatItem(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE, related_name="itemlari")
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    yetkazish_kuni = models.PositiveSmallIntegerField(default=4)
    yetkazish_puli = models.SmallIntegerField(default=30000)
    umumiy_summa = models.IntegerField(blank=True, null=True)
    def save(self, *args, **kwargs):
        narx = self.mahsulot.narx - (self.mahsulot.narx * self.mahsulot.chegirma/100)
        self.umumiy_summa = self.miqdor * narx + self.yetkazish_puli
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.mahsulot}"

class Buyurtma(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    holat = models.CharField(max_length=30)
    sana = models.DateField(auto_now_add=True)
    summa = models.IntegerField(null=True, blank=True)
    def save(self, *args, **kwargs):
        itemlari = self.savat.itemlari.all()
        self.summa =  itemlari.aggregate(summasi=Sum('umumiy_summa')).get('summasi')
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.profil}"