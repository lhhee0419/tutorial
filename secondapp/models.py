from django.db import models

class Hospital(models.Model):
    sido = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    medical=models.IntegerField()
    room=models.IntegerField()
    tel = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
