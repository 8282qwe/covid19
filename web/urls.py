from django.urls import path, include
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.Home_view, name="home"),
]