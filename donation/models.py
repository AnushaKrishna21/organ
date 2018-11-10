from django.db import models

class donor (models.Model):
	GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),)
	donor_id = models.CharField(primary_key=True,max_length=50)
	name = models.CharField(max_length=100,null=False,default=None)
	father_name = models.CharField(max_length=100,null=False,default=None)
	address = models.CharField(max_length=200,null=False,default=None)
	city = models.CharField(max_length=100,null=False,default=None)
	state = models.CharField(max_length=100,null=False,default=None)
	phno = models.IntegerField(max_length=15,null=False,default=None)
	email = models.CharField(max_length=100,null=False,default=None)
	age = models.IntegerField(max_length=5,null=False,default=None)
	gender  = models.CharField(max_length=1,choices=GENDER,null=False,default=None)
	blood = models.CharField(max_length=5,null=False,default=None)
	organ_name = models.CharField(max_length=100,null=False,default=None)