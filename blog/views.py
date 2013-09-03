from django.http import HttpResponse
from django.shortcuts import render

def Main(request):
	return render(request, "main.html",)

def Hello(request):
	return render(request, "hello.html",)
