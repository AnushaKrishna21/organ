from django.db import models
from donation.models import donor

class all_organs (models.Model):
	organ_id=models.CharField(max_length=50,primary_key=True,null=False,default=None)
	blood = models.CharField(max_length=4,null=False,default=None)
	received_from = models.ForeignKey(donor,related_name="all_organ_recieved_from",on_delete=models.CASCADE,null=True)
	received_date = models.CharField(max_length=15,null=False,default=None)
	donated_to = models.ForeignKey(donor,on_delete=models.CASCADE,null=True)
	donated_date = models.CharField(max_length=15,null=False,default=None)
	available_place = models.CharField(max_length=100,null=False,default=None)

class liver (models.Model):
	organ_id = models.ForeignKey(all_organs,on_delete=models.CASCADE)
	viral_testing = models.CharField(max_length=200,null=True,default=None)

class eyes (models.Model):
	organ_id = models.ForeignKey(all_organs,on_delete=models.CASCADE)
	unfit = models.CharField(max_length=200,null=True,default=None)

class kidney (models.Model):
	organ_id = models.ForeignKey(all_organs,on_delete=models.CASCADE)
	family = models.CharField(max_length=100,null=True,default=None)
	cadaver = models.CharField(max_length=100,null=False,default=None)