from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ediaries import decorators
from django.contrib.auth.decorators import user_passes_test
from .forms import SignUpForm, UpdateProfileForm


# Logout required decorators
def logout_required(function=None, logout_url=None):
    """
    Decorator for views that checks that the user is logged out, redirecting
    to the home page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=logout_url,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

# Create your views here.


@logout_required(logout_url='/')
def sign_up(request):
    form = SignUpForm()
    registered = False

    if request.method == 'POST':
        form_data = SignUpForm(data=request.POST)

        if form_data.is_valid():
            form_data.save()
            registered = True

    dictionary = {
        'form': form,
        'registered': registered
    }
    return render(request, 'app_login/sign_up.html', context=dictionary)


@logout_required(logout_url='/')
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


@login_required(login_url='/account/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='/account/login/')
def profile(request):
    return render(request, 'app_login/profile.html', context={})


@login_required(login_url='/account/login/')
def update_profile(request):
    current_user = request.user
    form = UpdateProfileForm(instance=current_user)

    if request.method == 'POST':
        form = UpdateProfileForm(data=request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UpdateProfileForm(instance=current_user)

    dictionary = {
        'form': form,
    }

    return render(request, 'app_login/update_profile.html', context=dictionary)
