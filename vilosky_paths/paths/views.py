from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'paths/home.html')

def search(request):
	return render(request, 'paths/search.html')
	
def dashboard(request):
	return render(request, 'paths/dashboard.html')

