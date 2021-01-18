from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request,'intro.html')

def view(request):
    return render(request,'view.html')

def register(request):
    return render(request,'register.html')

def check(request):
    return render(request,'check.html')
