from django.urls import path
from .views import home, success , donations

urlpatterns = [
    path('', home, name='home'),
    path('donations', donations, name='donations'),


    path('success' , success , name='success')
]