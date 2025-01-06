from django.shortcuts import render,redirect
from django.contrib import messages
from Notes.Templates import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        da = request.POST
        i = da.get('U_Id')
        T = da.get('Title')
        Text = da.get('Text')
        test.objects.create(
            U_Id = i,
            Title = T,
            Text = Text
        )
        return redirect('/index/')
    ooj = request.GET.get('U_Id')
    object = test.objects.filter(U_Id = ooj)
    print(object)
    return render(request,"Index.html",{'t':object})
    
@login_required(login_url='/login/')
def remove(request, id):
    item = test.objects.get(id = id)
    item.delete()
    return redirect('/index/')

@login_required(login_url='/login/')
def update(request,id):
    item = test.objects.get(id = id)
    da = request.POST
    if request.method == 'POST':
        item.Title = da.get('Title')
        item.Text = da.get('Text')
        item.save()
        return redirect('/index/')
    return render(request,'update.html',{'context':item})

def registration_page(request):
    if request.method == 'POST':
        da = request.POST
        User_Name = da.get('User_Name')
        Last_Name = da.get('Last_Name')
        First_Name = da.get('First_Name')
        Password = da.get('Password')
       
        if not User.objects.filter(username = User_Name).exists():
            user = User.objects.create(
                first_name = First_Name,
                last_name = Last_Name,
                username = User_Name
            )
            user.set_password(Password)
            user.save()
            messages.info(request, "User created successfully")
            return redirect('/login/')
        else:
            messages.info(request, "User-Name already exists !!!")
        
    return render(request,'Registration.html')

def login_page(request):
    if request.method == 'POST':
        da = request.POST
        username = da.get('User_Id')
        password = da.get('Password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid User-Name !!!")

        User.objects.filter(username = "").delete()

        u1 = authenticate(username = username,password = password)
        
        if u1 is None:
            return redirect('/login/')
        else:
            login(request,u1)
            return redirect('/index/')
    return render(request,'Login.html')

@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return redirect('/login')