from django import forms
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from .models import boodleReceiver


class boodleReceiverForm(forms.ModelForm):
	class Meta:
		model = boodleReceiver
		fields = '__all__'


class LoginForm(forms.Form):
	username = forms.CharField(label="User Name",max_length=15)
	password = forms.CharField(widget=forms.PasswordInput())


class boodleRunnerForm(forms.Form):
	runnerName = forms.CharField(label='Name',max_length=50)
	runnerPhoneNumber = forms.IntegerField(label='Phone Number')
	runnerBarracks = forms.CharField(label='Barracks',max_length=10)
	runnerCompany = forms.CharField(label='Company', max_length=2)
