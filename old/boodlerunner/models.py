from django.db import models
from django.contrib.auth.models import User


class boodleReceiver(models.Model):
	name = models.CharField(max_length=50)
	phoneNumber = models.IntegerField()
	barracks = models.CharField(max_length=10)
	roomNumber = models.IntegerField()
	restaurant = models.CharField(max_length=50)
	timeOfArrival = models.IntegerField()
	additionalInstruction = models.CharField(max_length=250)
	receiverCompany = models.CharField(max_length=2)

class boodleRunner(models.Model):
	runnerName = models.CharField(max_length=50)
	runnerPhoneNumber = models.IntegerField()
	runnerBarracks = models.CharField(max_length=10)
	runnerCompany = models.CharField(max_length=2)


class boodleRequest(models.Model):
	id = models.CharField(max_length=50,primary_key=True)
	receiverID = models.ForeignKey(boodleReceiver, on_delete=models.CASCADE)
	runnerID  =  models.ForeignKey(boodleRunner, on_delete=models.CASCADE)