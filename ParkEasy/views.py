from django.shortcuts import render,redirect
from ParkEasy.Templates import *

# Create your views here.
def index(request):
    return render(request,'index1.html')