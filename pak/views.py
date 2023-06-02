from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def babar(request):
    return render(request,'babar.html')

def babar_bat(request):
    return HttpResponse('babar is a good player')