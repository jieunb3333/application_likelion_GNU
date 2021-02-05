from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def intro(request):
    
    return render(request,'intro.html')

def view(request):
    return render(request,'view.html')

def register(request):
    user_id=request.GET.get('user_id')
    print(user_id)
    return render(request,'register.html')

def register_action(request):
    inform=User()
    inform.user_name=request.POST['name']
    inform.user_pn=request.POST['phonenumber']
    inform.user_grade=request.POST['grade']
    inform.user_major=request.POST['major']
    inform.user_q1=request.POST['q1']
    inform.user_q2=request.POST['q2']
    inform.user_q3=request.POST['q3']
    inform.user_q4=request.POST['q4']
    inform.save()
    return redirect('/register_check/')

def register_check(request):
    inform=User.objects.filter(pk=3)
    return render(request,'register_check.html',{'inform':inform})

def check(request):
    # #user_id 받아주기 
    # #check 페이지 전 데이터 보낼때 <input type='hidden' value={{profile.getId()}} name='user_id'> 추가
    # #user_id=request.GET.get('user_id')
    # if(user_id=='null'):
    #     return render(request,'intro.html')
    #     #user_id가 존재하지 않으면 intro로 이동. / 로그인부터 하도록 함.
    
    # else:
    #     inform=User.objects.filter(pk=user_id) #추후에 pk user_id로 바꾸기
    #     return render(request,'check.html',{'inform':inform})
    #     #현재 로그인 한 계정의 user_id를 비교하여 사용자 정보를 가져옴
    # ctrl / 주석
    inform=User.objects.all
    return render(request,'check.html',{'inform':inform})


    
    
