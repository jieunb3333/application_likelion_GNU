from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def intro(request):
    return render(request, "intro.html")


def view(request):
    return render(request, "view.html")


def register(request):
    google_id = request.session["google_id"]
    inform = User.objects.filter(user_id=google_id)
    return render(request, "register.html",{"inform": inform})


def register_action(request):
    checkbox_value=request.POST["checkbox_value"]
    google_id = request.POST["googleID"]
    if checkbox_value =='no_checked':
        if User.objects.filter(user_id=google_id).exists()==True:
            inform = User.objects.get(user_id=google_id)
        else: inform = User()
        inform.user_id = google_id
        inform.user_name = request.POST["name"]
        inform.user_pn = request.POST["phonenumber"]
        inform.user_grade = request.POST["grade"]
        inform.user_major = request.POST["major"]
        inform.user_q1 = request.POST["q1"]
        inform.user_q2 = request.POST["q2"]
        inform.user_q3 = request.POST["q3"]
        inform.user_q4 = request.POST["q4"]
        inform.save()
        request.session["google_id"] = google_id
        return render(request, "register.html",{"inform": inform})
    else:
        if User.objects.filter(user_id=google_id).exists()==True:
            inform = User.objects.filter(user_id=google_id)
        else: inform = User() 
        inform.user_id = google_id
        inform.user_name = request.POST["name"]
        inform.user_pn = request.POST["phonenumber"]
        inform.user_grade = request.POST["grade"]
        inform.user_major = request.POST["major"]
        inform.user_q1 = request.POST["q1"]
        inform.user_q2 = request.POST["q2"]
        inform.user_q3 = request.POST["q3"]
        inform.user_q4 = request.POST["q4"]
        inform.save()
        request.session["google_id"] = google_id
        return redirect("/register_check")
    


def register_check(request):
    google_id = request.session["google_id"]
    inform = User.objects.filter(user_id=google_id)
    print(google_id)
    return render(request, "register_check.html", {"inform": inform})


def check(request):
    return render(request, "check.html")
