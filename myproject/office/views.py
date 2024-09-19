from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, TaskUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
        ]

def login(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth_login(request,user)
            return redirect("welcome")
            #print(user)
    else:
        form=AuthenticationForm()
    
    return render(request,"login.html", {"form":form})


def welcome(request):
    return render(request, "welcome.html")

def home(request):

    
    info = Task.objects.all()
    
   
    return render(request, "home.html", {"info": info})
def details(request, pk):
    try:

        info = Task.objects.get(pk=pk)
        return render(request, "details.html", {"info": info})
    except Task.DoesNotExist:
        return HttpResponse("person does not exist")


def update_page(request):
    info = Task.objects.all()
    return render(request,"update_page.html",{"info":info})


def delete_page(request):
    info = Task.objects.all()
    return render(request,"delete_page.html",{"info":info})

def delete_info(request, pk):
    try:
        info = Task.objects.get(pk=pk)
        info.delete()
        return redirect("delete_page")
    except Task.DoesNotExist:
        return HttpResponse("info does not exist")
    
 
def start(request):
    return render (request, "start.html")

def registration(request):
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
         form=UserCreationForm()
    context={
        "form":form,
    }
    return render(request, "register.html",context )

def form(request):
    if request.method == "POST":
        form  = TaskForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("home")
    else:

        form= TaskForm()
        return render(request, "form.html", {"form":form})

def update(request, pk):
    try:
        info = Task.objects.get(pk=pk)

        if request.method == "POST":
            info_form = TaskUpdateForm(request.POST, instance=info)
            if info_form.is_valid():
                info_form.save()
                return redirect("home")
            else:
                context = {
                    "form": info_form,
                }
                return render(request, "update.html", context=context)

        info_form = TaskUpdateForm(instance=info)
        return render(request, "update.html", {"form": info_form})
    except Task.DoesNotExist:
        return HttpResponse("Info does not exist")