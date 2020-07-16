from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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