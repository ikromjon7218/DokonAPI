from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    J = [('erkak', 'erkak'),
        ('ayol', 'ayol')]
    ism = models.CharField(max_length=50)
    rasm = models.FileField(max_length=50)
    tel = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tugilgan_yil = models.PositiveIntegerField()
    jins = models.CharField(max_length=5, choices=J, null=True)
    shahar = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.ism}"