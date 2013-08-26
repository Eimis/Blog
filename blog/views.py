from django.http import HttpResponse
from django.shortcuts import render

def Hello(request):
	"""
	TODO: admin, template
	"""
	return render(request, "index.html")