from django import forms

class boodleReceiverForm(forms.Form):
	name = forms.CharField(label='Name',max_length=50)
	phoneNumber = forms.CharField(label='Your Phone Number',)
	barracks = forms.CharField(label='Barracks',max_length=10)
	roomNumber = forms.CharField(label='Room Number',)
	restaurant = forms.CharField(label='Restaurant',max_length=50)
	timeOfArrival = forms.CharField(label='Time of Arrival',)
	additionalInstruction = forms.CharField(label='Additional instruction for runner',max_length=250)
	receiverCompany = forms.CharField(label='Your company',max_length=2)



class LoginForm(forms.Form):
	username = forms.CharField(label="User Name",max_length=15)
	password = forms.CharField(widget=forms.PasswordInput())


class boodleRunnerForm(forms.Form):
	runnerName = forms.CharField(label='Name',max_length=50)
	runnerPhoneNumber = forms.CharField(label='Phone Number')
	runnerBarracks = forms.CharField(label='Barracks',max_length=10)
	runnerCompany = forms.CharField(label='Company', max_length=2)
