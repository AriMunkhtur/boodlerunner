from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import LoginForm
from .forms import boodleReceiverForm
from .forms import boodleRunnerForm
from django.http import HttpResponseRedirect
from .models import boodleReceiver


def welcome(request):
    return render(request, 'boodlerunner/welcome.html', {})
    #form = boodleReceiverForm()
    #return render(request, 'boodlerunner/welcome.html','boodleReceiverInfo': receiverInfo, 'forms':form)

def menu(request):
	return render(request, 'boodlerunner/menu.html', {})




def updateRunner(request):
	form = boodleRunnerForm(request.POST  or None)
	if form.is_valid():
		runnerInfo  = boodleRunner(name = forms.cleaned_data['name'],
										phoneNumber  = forms.cleaned_data['phone number'],
										barracks =   forms.cleaned_data['barracks'],
										runnerCompany = forms.cleaned_data['company'],)
		runnerInfo.save()
	return render(request,'boodlerunner/runner.html',{'form': form})

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


def receipt(request, order_id):
	orders = boodleReceiver.objects.all()
	form = boodleReceiverForm()
	return render(request, 'boodlerunner/receipt.html', {'orders':orders, 'form':form})


def order(request):
	orders = boodleReceiver.objects.all()
	form = boodleReceiverForm()
	return render(request,'boodlerunner/order.html',{'orders':orders,'form':form})


def post_order(request):
	form = boodleReceiverForm(request.POST)
	if form.is_valid():
		receiverInfo  = boodleReceiver(name = form.cleaned_data['name'],
										phoneNumber = form.cleaned_data['phoneNumber'],
										barracks =   form.cleaned_data['barracks'],
										roomNumber =  form.cleaned_data['roomNumber'],
										restaurant =  form.cleaned_data['restaurant'],
										timeOfArrival =   form.cleaned_data['timeOfArrival'],
										additionalInstruction =   form.cleaned_data['additionalInstruction'],
										receiverCompany =   form.cleaned_data['receiverCompany'],)
		receiverInfo.save()
	return HttpResponseRedirect('boodlerunner/receipt.html')