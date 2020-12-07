from django.urls import path
from . import views

app_name = 'webhook'
urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('exchangeRate/', views.exchangeRate, name='exchangeRate'),
]