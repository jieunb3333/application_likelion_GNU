from django.contrib import messages
from django.shortcuts import render, redirect, reverse, Http404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Inform
import requests

# Create your views here.
def intro(request):
    return render(request, "intro.html")

def login_action(request):
    token = request.GET.get('token')
    r = requests.get('https://oauth2.googleapis.com/tokeninfo?id_token='+token)
    #curl로 token을 user_id로 만들기
    user_id = r.json()['sub']
    print(user_id)

    try:
        user = User.objects.get(username=user_id)
    except User.DoesNotExist:
        user = User.objects.create(username=user_id)
        user.set_unusable_password()
        user.save()

    login(request, user)


    #if informs에 내가 작성한게 있으면 
    if Inform.objects.filter(user__username=user_id).exists():
        return redirect('/register_check')
    else:
        return redirect('/register')

def check_action(request):
    token = request.GET.get('token')
    r = requests.get('https://oauth2.googleapis.com/tokeninfo?id_token='+token)
    #curl로 token을 user_id로 만들기
    user_id = r.json()['sub']
    print(user_id)

    try:
        user = User.objects.get(username=user_id)
    except User.DoesNotExist:
        user = User.objects.create(username=user_id)
        user.set_unusable_password()
        user.save()

    login(request, user)


    #if informs에 내가 작성한게 있으면 
    if Inform.objects.filter(user__username=user_id).exists():
        return redirect('/check')
    else:
        messages.add_message(request, messages.ERROR, 'ERROR')
        return redirect('/')


def view(request):
    return render(request, "view.html")


def register(request):

#     google_id = request.session["google_id"]
#     inform = User.objects.filter(user_id=google_id)
#     return render(request, "register.html",{"inform": inform})

    #구글에 방금 받은 토큰에 대해서 물어보기
    #curl 이용
    
    if request.user.is_authenticated:
        if Inform.objects.filter(user__username=request.user).exists():
            return redirect('/register_check')
        else:
            return render(request, "register.html")
        
    else:
        messages.add_message(request, messages.ERROR, '잘못된 접근입니다. 로그인 후 이용해주세요')
        return redirect('/')



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
    if request.user.is_authenticated:
        if Inform.objects.filter(user__username=request.user).exists():
            inform = request.user.informs
            return render(request, "register_check.html", {"inform": inform})
        else:
            return redirect('/register')
    else:
        messages.add_message(request, messages.ERROR, '잘못된 접근입니다. 로그인 후 이용해주세요')
        return redirect('/')
    



def check(request):
    print(request.user)
    if request.user.is_authenticated:
        if Inform.objects.filter(user__username=request.user).exists():
            inform = request.user.informs
            return render(request, 'check.html', {"inform": inform})
        else:
            return redirect('/register')
    else:
        messages.add_message(request, messages.ERROR, '잘못된 접근입니다. 로그인 후 이용해주세요')
        return redirect('/')




