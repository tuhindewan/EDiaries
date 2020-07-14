from django.shortcuts import render

# Create your views here.

def index(request):
    dictionary = {

    }
    return render(request, 'app_blog/index.html', context=dictionary)
