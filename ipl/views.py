from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sachin(request):
    return render(request,'sachin.html')

def sachin_bat(request):
    return HttpResponse('god of the cricket')