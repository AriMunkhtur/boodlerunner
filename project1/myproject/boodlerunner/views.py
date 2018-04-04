from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def welcome(request):
    return render(request, 'boodlerunner/welcome.html', {})

def signup(request):
    form = UserCreationForm()
    return render(request, 'boodlerunner/signup.html', {'form': form})