from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	text = "This is the home page.<br>"
	text += "<a href='/paths/search/'>Go to the Search Page</a><br>"
	text += "<a href='/paths/dashboard/'>Go to the Dashboard</a><br>"
	return HttpResponse(text)

def search(request):
	return HttpResponse("This is the search page")
	
def dashboard(request):
	return HttpResponse("This is the dashboard")

