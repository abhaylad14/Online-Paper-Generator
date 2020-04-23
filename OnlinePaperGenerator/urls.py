from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('registeration/', views.registeration, name="registeration"),
    path('handlelogin/', views.handlelogin, name="handlelogin"),
    path('handlelogout/', views.handlelogout, name="handlelogout"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('adminhome/allocatesubject/', views.allocatesubject, name="allocatesubject"),
    path('adminhome/allocatefaculty/', views.allocatefaculty, name="allocatefaculty"),
    path('adminhome/subjectmanager/', views.subjectmanager, name="subjectmanager"),
    path('home/<str:uname>/', views.home, name="userhome"),
]
