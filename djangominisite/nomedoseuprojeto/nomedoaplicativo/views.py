from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    #return HttpResponse('Olá, mundo!')
    #message = 'hello, world'
    #return render(request,'index.html',{'message':message})
    colors = ['red', 'blue', 'green']
    return render(request, 'index.html', {'colors': colors})

def input_form(request):
    if request.method == 'POST':
        try:
            num1 = int(request.POST['num1'])
            num2 = int(request.POST['num2'])
            result = num1 + num2
        except:
            result = 0    
        return render(request, 'input_form.html', {'result': result})

    return render(request, 'input_form.html')