from django.db import models
from django.contrib.auth.models import User


class boodleReceiver(models.Model):
	user = models.OneToOneField(User,  on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	phoneNumber = models.CharField(max_length=25)
	barracks = models.CharField(max_length=10)
	roomNumber = models.CharField(max_length=25)
	receiverCompany = models.CharField(max_length=2)
	def __str__(self):
		return (self.name)

class boodleRunner(models.Model):
	user = models.OneToOneField(User,  on_delete=models.CASCADE)
	runnerName = models.CharField(max_length=50)
	runnerPhoneNumber = models.CharField(max_length=25)
	runnerBarracks = models.CharField(max_length=10)
	runnerCompany = models.CharField(max_length=2)
	def __str__(self):
		return (self.runnerName)


class boodleRequest(models.Model):
	receiver = models.ForeignKey(boodleReceiver, on_delete=models.CASCADE)
	runner  =  models.ForeignKey(boodleRunner, on_delete=models.CASCADE)
	restaurant = models.CharField(max_length=50)
	timeOfArrival = models.CharField(max_length=25)
	additionalInstruction = models.CharField(max_length=250)
