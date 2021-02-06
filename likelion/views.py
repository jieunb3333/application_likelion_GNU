from django.contrib import messages
from django.shortcuts import render, redirect, reverse, Http404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Inform

# Create your views here.
def intro(request):
    return render(request, "intro.html")

def login_ajax(request):
    if request.POST:
        user_id = request.POST.get('user_id')
        
        try:
            user = User.objects.get(username=user_id)
        except User.DoesNotExist:
            user = User.objects.create(username=user_id)
            user.set_unusable_password()
            user.save()

        login(request, user)
        return redirect(reverse('register'))


def view(request):
    return render(request, "view.html")


def register(request):
    if request.user.is_authenticated:
        return render(request, "register.html")
    else:
        messages.add_message(request, messages.ERROR, '잘못된 접근입니다. 로그인 후 이용해주세요')
        return redirect('intro')


def register_action(request):
    checkbox_value=request.POST["checkbox_value"]

    if checkbox_value =='no_checked':
        return redirect("/register/#check")
    else:
        inform = Inform()
        inform.user = request.user
        inform.user_name = request.POST["name"]
        inform.user_pn = request.POST["phonenumber"]
        inform.user_grade = request.POST["grade"]
        inform.user_major = request.POST["major"]
        inform.user_q1 = request.POST["q1"]
        inform.user_q2 = request.POST["q2"]
        inform.user_q3 = request.POST["q3"]
        inform.user_q4 = request.POST["q4"]
        inform.save()
        request.user.inform = inform
        return redirect("/register_check")
    


def register_check(request):
    print(request.user)
    inform = request.user.informs
    return render(request, "register_check.html", {"inform": inform})


def check(request):
    return render(request, "check.html")
