from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import LoginForm
from .forms import boodleReceiverForm


def welcome(request):
    return render(request, 'boodlerunner/welcome.html', {})
    #form = boodleReceiverForm()
    #return render(request, 'boodlerunner/welcome.html','boodleReceiverInfo': receiverInfo, 'forms':form)


def order(request):
	form = boodleReceiverForm(request.POST  or None)
	if form.is_valid():
		receiverInfo  = boodleReceiver(name = forms.cleaned_data['name'],
										phoneNumber  = forms.cleaned_data['phone number'],
										barracks =   forms.cleaned_data['barracks'],
										roomNumber =   forms.cleaned_data['room number'],
										restaurant =   forms.cleaned_data['restaurant'],
										timeOfArrival =   forms.cleaned_data['time of arrival'],
										additionalInstruction =   forms.cleaned_data['additional instruction'],
										receiverCompany = forms.cleaned_data['company'],)
		receiverInfo.save()
	return render(request,'boodlerunner/order.html',{'form': form})


def signup(request):
    form = UserCreationForm()
    return render(request, 'boodlerunner/signup.html', {'form': form})

def loginPage(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'boodlerunner/order.html', {'form':form})

				else:
					print("disabled")
			else:
				print('incorrect')
	else:
		form =LoginForm()
		return render(request, 'boodlerunner/order.html',{'form':form})



#def post_boodleReceiverInfo(request):
#	form = boodleReceiverForm(request.POST)
#	if form.is_valid():
#		receiverInfo  = boodleReceiver(name = forms.cleaned_data['name'],
#										phoneNumber  = forms.cleaned_data['phone number'],
#										barracks =  = forms.cleaned_data['barracks'],
#										roomNumber =  = forms.cleaned_data['room number'],
#										restaurant =  = forms.cleaned_data['restaurant'],
#										timeOfArrival =  = forms.cleaned_data['time of arrival'],
#										additionalInstruction =  = forms.cleaned_data['additional instruction'],
#										receiverCompany = f = forms.cleaned_data['company'],)
#		receiverInfo.save()
#	return HttpResponseRedirect('boodlerunner/welcome.html')