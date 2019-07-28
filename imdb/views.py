from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"index.html")

def addmovie(request):
	return render(request,"addmovie.html")

