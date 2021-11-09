from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.

def fnHello(request):
    return HttpResponse("hello i am Ragisha")

def fnSample(request):
    if request.method=='POST':
        name=request.POST['n1']
        age=request.POST['n2']
        usOBJ=sample(name=name,age=age)
        usOBJ.save()
    return render(request, 'sample.html')
def fnSample2(request):
    return render(request,'sample2.html')
    