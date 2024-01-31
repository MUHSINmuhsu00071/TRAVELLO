from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def fun(request):
    obj=place()
    obj.name="suite"
    return render(request,'house.html',{'result':obj})