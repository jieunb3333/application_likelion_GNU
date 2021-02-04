from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def intro(request):

    return render(request, "intro.html")


def view(request):
    return render(request, "view.html")


def register(request):
    return render(request, "register.html")


def register_action(request):

    inform = User()
    google_id = request.POST["googleID"]
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
    return redirect("/register_check/")


def register_check(request):
    google_id = request.session["google_id"]
    inform = User.objects.filter(user_id=google_id)
    return render(request, "register_check.html", {"inform": inform})


def check(request):
    return render(request, "check.html")
