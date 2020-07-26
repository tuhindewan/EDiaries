from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update'),
    path('password/', views.update_password, name='update_password'),
]
