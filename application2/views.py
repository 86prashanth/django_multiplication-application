from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h2>This is direct display message')

def func(request):
    return render(request,'app/home.html'),