from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fnHello(request):
    return HttpResponse("hello i am Ragisha")

def fnSample(request):
    return render(request, 'sample.html')
def fnSample2(request):
    return render(request,'sample2.html')
    