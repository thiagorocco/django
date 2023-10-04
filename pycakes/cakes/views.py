from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'cakes/home.html')