from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import User, CustomUserManager
from .forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            return redirect('/login/')

    else:
        form = RegistrationForm()

    return render(request, 'userprofile/signup.html', {
        'form' : form
    })
