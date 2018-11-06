from django.db import models

class Hospital(models.Model):
    Hid = models.CharField(max_length=100)
    Hname = models.CharField(max_length=500)
    Address = models.CharField(max_length=1000)
    Ph_no = models.IntegerField(max_length=15)
    Uname = models.CharField(max_length=100)
    Pwd = models.CharField(max_length=100)
