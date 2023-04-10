from django.db import models
from userapp.models import *

class Bolim(models.Model):
    nom = models.CharField(max_length=15)
    rasm = models.FileField(blank=True, null=True)
    def __str__(self):
        return f"{self.nom}"

class Mahsulot(models.Model):
    nom = models.CharField(max_length=15)
    narx = models.PositiveIntegerField()
    chegirma = models.SmallIntegerField()
    brend = models.CharField(max_length=15)
    batafsil = models.CharField(max_length=200)
    rasm = models.FileField(blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    holat = models.CharField(max_length=20)
    mavjud = models.BooleanField(default=True)
    sotuvchi = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.nom}"

class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    matn = models.CharField(max_length=200)
    reyting = models.SmallIntegerField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    sana = models.DateField()
    def __str__(self):
        return f"{self.profil}"


