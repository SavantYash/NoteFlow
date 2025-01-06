"""
URL configuration for test12 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home') 
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Notes import views 
from ParkEasy import views as pe
from FunGrow import views as fg
urlpatterns = [
    path('admin/', admin.site.urls),
]

Notes = [
    path('index/',views.index),
    path('del/<int:id>', views.remove, name="del"),
    path('update/<int:id>',views.update, name="update"),
    path('registration/',views.registration_page,name="registration"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name = "logout")
]

ParkEasy = [
    path('pe/index/',pe.index)
]

FunnGro = [
    path('FunnGro/Teen',fg.home)
]

urlpatterns = urlpatterns + Notes + ParkEasy + FunnGro;