from django.urls import path
from . import views

app_name = 'webhook'
urlpatterns = [
    path('webhook/', views.webhook, name='webhook'),
]