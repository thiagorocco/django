from django.shortcuts import render


def angular_demo(request):
    return render(request, 'myapp/index.html')
