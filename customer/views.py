from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('favas')

def head(request):
    return render(request,'customer\cust.html')   

def cus(request):
    return render(request,'customer\cust2.html')     
