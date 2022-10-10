from django.urls import path
from .views import *

urlpatterns = [
    path('',where,name='home'),
    path('where/',There,name='there'),
]
