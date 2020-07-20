from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login')
]