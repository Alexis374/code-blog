__author__ = 'ljcbeyond'
from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return render(request,'test/second.html')
