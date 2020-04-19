import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student_management_app.EmailBackEnd import EmailBackEnd

# Create your views here.
def showDemoPage(request):
    return render(request, "demo.html")

def showLoginPage(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method!="POST":
        print(request)
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponse("EMAIL:"+request.POST.get("email")+" pass: "+request.POST.get("password"))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("director_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")