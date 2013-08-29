from django.http import HttpResponse
from django.shortcuts import render

def Hello(request):
	"""
	TODO: admin, DESIGN (template)
	"""
	return render(request, "main.html")