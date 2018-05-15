from django import forms
from crispy_forms.helper import FormHelper
from .models import boodleReceiver
from .models import boodleRunner
from .models import boodleRequest


class boodleReceiverForm(forms.ModelForm):
	name = forms.CharField(label='Name',max_length=50)
	phoneNumber = forms.IntegerField(label='Your Phone Number',)
	barracks = forms.CharField(label='Barracks',max_length=10)
	roomNumber = forms.IntegerField(label='Room Number',)
	receiverCompany = forms.CharField(label='Your company',max_length=2)

	def __init__(self, *args, **kwargs):
		super(boodleReceiverForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
	class Meta:
		model = boodleReceiver
		fields = ['name', 'phoneNumber', 'barracks', 'roomNumber', 'receiverCompany']

class LoginForm(forms.Form):
	username = forms.CharField(label="User Name",max_length=15)
	password = forms.CharField(widget=forms.PasswordInput())


class boodleRunnerForm(forms.ModelForm):
	runnerName = forms.CharField(label='Name',max_length=50)
	runnerPhoneNumber = forms.IntegerField(label='Phone Number')
	runnerBarracks = forms.CharField(label='Barracks',max_length=10)
	runnerCompany = forms.CharField(label='Company', max_length=2)
	def __init__(self, *args, **kwargs):
		super(boodleRunnerForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
	class Meta:
		model = boodleRunner
		fields = ['runnerName', 'runnerPhoneNumber', 'runnerBarracks', 'runnerCompany']

class boodleRequestForm(forms.ModelForm):
    class Meta:
        model = boodleRequest
        fields = ['runner', 'restaurant', 'timeOfArrival', 'additionalInstruction']