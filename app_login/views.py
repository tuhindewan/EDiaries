from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def sign_up(request):
    form = UserCreationForm()
    registered = False
    
    if request.method == 'POST':
        form_data = UserCreationForm(data=request.POST)

        if form_data.is_valid():
            form_data.save()
            registered = True

    dictionary = {
        'form': form,
        'registered': registered
    }
    return render(request, 'app_login/sign_up.html', context=dictionary)


def user_login(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form_data = AuthenticationForm(data=request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    dictionary = {
        'form': form,
    }
    return render(request, 'app_login/login.html', context=dictionary)