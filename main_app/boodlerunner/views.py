from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import LoginForm
from .forms import boodleReceiverForm
from .forms import boodleRunnerForm
from .forms import boodleRequestForm
from .models import boodleReceiver
from .models import boodleRunner
from .models import boodleRequest

def welcome(request):
    return render(request, 'boodlerunner/welcome.html', {})
    #form = boodleReceiverForm()
    #return render(request, 'boodlerunner/welcome.html','boodleReceiverInfo': receiverInfo, 'forms':form)

def menu(request):
    return render(request, 'boodlerunner/menu.html', {})

def order(request):
    form = boodleRequestForm(request.POST  or None)
    
    return render(request,'boodlerunner/order.html',{'form': form})


def updateRunner(request):
    if request.method == "POST":
        form = boodleRunnerForm(request.POST)
        if form.is_valid():
            runnerInfo  = boodleRunner(name = form.cleaned_data['name'],
                                        phoneNumber  = form.cleaned_data['phone number'],
                                        barracks =   form.cleaned_data['barracks'],
                                        runnerCompany = form.cleaned_data['company'],)
            runnerInfo.save()
    else:
        if request.user.is_authenticated:
            try:
                runner = boodleRunner.objects.get(user=request.user)
            except:
                runner = boodleRunner()
                runner.user = request.user
                runner.save()
        form = boodleRunnerForm()
    return render(request,'boodlerunner/runner.html',{'form': form})

def updateReceiver(request):
    if request.method == "POST":
        form = boodleReceiverForm(request.POST)
        if form.is_valid():
            br = form.save(commit=False)
            receiver = boodleReceiver.objects.get(user=request.user)
            receiver.name = br.name
            receiver.phoneNumber = br.phoneNumber
            receiver.barracks = br.barracks
            receiver.roomNumber = br.roomNumber
            receiver.receiverCompany = br.receiverCompany
            receiver.save()
            return render(request,'boodlerunner/menu.html')
    else:
        if request.user.is_authenticated:
            try:
                receiver = boodleReceiver.objects.get(user=request.user)
            except:
                receiver = boodleRunner()
                receiver.user = request.user
                receiver.save()
        print (receiver.name)
        form = boodleReceiverForm(instance=receiver)
    return render(request,'boodlerunner/runner.html',{'form': form})

def deliver(request):
    orders = boodleRequest.objects.all()
    return render(request, 'boodlerunner/delivery.html')

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



def receipt(request):

    return render(request, 'boodlerunner/receipt.html', {})

def get_order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = boodleRequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            receiverInfo = form.save(commit=False)
            print("form is valid")
            receiver = boodleReceiver.objects.get(user=request.user)
            receiverInfo.receiver = receiver
            receiverInfo.save()
        else:
            print ("Form isn't valid")
        return render(request, 'boodlerunner/receipt.html', {'receiverInfo': receiverInfo})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = boodleReceiverForm()
        return render(request, 'boodlerunner/receipt.html', {'form': form})



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