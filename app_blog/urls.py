from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.index, name='app_blog_index'),
]