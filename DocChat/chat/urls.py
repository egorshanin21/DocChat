from django.urls import path
from .views import home

app_name ='chat'

urlpatterns = [
    path('', home, name='home'),
]