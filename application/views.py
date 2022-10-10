from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def where(request):
    return HttpResponse('<h1>this is text</h1>')

def There(request):
    return render(request,'app/home.html')