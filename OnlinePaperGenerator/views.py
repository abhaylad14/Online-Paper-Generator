from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import re 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
import json

# Create your views here.
#home Page for welcome users 
def index(request):
    return render(request, "home.html")

#Registration process
def registeration(request):
    # Arrived data 
    if request.method == "POST":
        remail = request.POST['emailid']
        rpass1 = request.POST['pass1']
        rpass2 = request.POST['pass2']
        fname = request.POST['fname']
        lname = request.POST['lname']
        username =  request.POST['uname']
        
        #form validations

        #flags for the validations
        userflag = fnameflag = lnameflag = emailflag = pass1flag = passwordflag = False
        #userame validations
        if len(username) > 10:
            messages.error (request, "Length of username must be less than 10")
            return redirect("home")
        else:
            if len(username) < 4:
                messages.error (request, "Length of username must be greater than 4")
                return redirect("home")
            else:
                userflag = True
        userobj = User.objects.filter(username = username)
        if len(userobj) > 0:
            messages.error (request, "The User already exists")
            userflag = False
            return redirect("home")
        else:
            userflag = True

        #firstname validations
        if len(fname) > 20:
            messages.error (request, "Length of Firstname must be less than 20")
            return redirect("home")
        else:
            if len(fname) < 2:
                messages.error (request, "Length of Firstname must be greater than 2")
                return redirect("home")
            else:
                fnameflag = True

        #lastname validations
        if len(lname) > 20:
            messages.error (request, "Length of Lastname must be less than 20")
            return redirect("home")
        else:
            if len(lname) < 2:
                messages.error (request, "Length of Lastname must be greater than 2")
                return redirect("home")
            else:
                lnameflag = True
        
        #email validations
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        def check(email):  
            if(re.search(regex,email)):
                return True
            else:  
                return False
        if check(remail):
            emailflag = True
        else:
            messages.error (request, "Pleas provide a velid email address")
            return redirect("home")

        #password validation
        if len(lname) > 20:
            messages.error (request, "Length of Lastname must be less than 20")
            return redirect("home")
        else:
            if len(rpass1) < 6:
                messages.error (request, "Length of Password must be greater than 6")
                return redirect("home")
            else:
                pass1flag = True

        if rpass1 != rpass2:
            messages.error (request, "Pasword did not matched")
            return redirect("home")
        else:
            passwordflag = True

        #User creation
        if userflag == True and fnameflag == True and lnameflag == True and emailflag == True and pass1flag == True and passwordflag == True:
            myuser = User.objects.create_user(username,remail,rpass2)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "The user has been registered Successfully")
            return redirect("home") 
        else:
            messages.error (request, "Something went wrong, Please try again")
            return redirect("home")

    return HttpResponse("Error 404: Page not found")

#login Process
def handlelogin(request):
    # Arrived data 
    if request.method == "POST":
        loginuname = request.POST['uname']
        loginpass = request.POST['pass']
        user = authenticate(username=loginuname, password = loginpass)

        #checking that if user exists or not
        if user is not None:
            # What to do when user exists
            login(request,user)
            messages.success(request,"Login Successful, Welcome " + user.first_name)
            #home(request,user.username)
            request.session['username'] = user.username
            return redirect("userhome",user.username)
        else:
            messages.error(request, "Invalid Username or Password, Please try again")
            return redirect("home")

    return HttpResponse("Error 404: Page not found")

def handlelogout(request):
    try:
        del request.session['username']
    except:
      pass
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect("home")

#Home page for the admin
def adminhome(request):
    if request.user.is_superuser:
        return render(request,"admin/adminhome.html")
    else:
        return HttpResponse("Error 404: page not found")

#subject allocation
def allocatesubject(request):
    if request.user.is_superuser:
        sub = subject.objects.all()
        fac = User.objects.all()
        params = {
            "obj": sub,
            "faculty": fac
            }
        return render(request, "admin/allocatesubject.html",params)
    else:
        return HttpResponse("error 404: page not found")

#faculty allocation to a particular subject by AJAX
def allocatefaculty(request):
    if request.user.is_superuser:
        if request.method == "POST":
            #data received from web in the form of JSON
            #So we decode the JSON
            form_data = json.loads(request.body.decode())
            subjectcode = form_data["code"]
            subfaculty = form_data["fac"]
            obj = subject.objects.get(subject_code = subjectcode)
            subname = obj.subject_name
            obj.faculty = subfaculty
            obj.save()
            return HttpResponse("")
        return redirect("allocatesubject")
    else:
        return HttpResponse("error 404: page not found")

#Add/Remove Subjects
def subjectmanager(request):
    if request.user.is_superuser:
        sub = subject.objects.all()
        fac = User.objects.all()
        params = {
            "obj": sub,
            "faculty": fac
            }
        #Receive data from the web
        if request.method == "POST":
            subcode = request.POST["subjectcode"]
            subname = request.POST["subjectname"]
            sem = request.POST["sem"]
            print(subcode, subname, sem)
            temp = subject.objects.filter(subject_code = subcode)
            obj = subject(subject_code = subcode, subject_name = subname, sem = sem)
            if len(temp) == 0:
                obj.save()
                messages.success(request, subname + " saved")
            else:
                messages.error(request, subname + " is already present")

        return render(request, "admin/subjectmanager.html",params)
    else:
        return HttpResponse("error 404: page not found")

#home page for the faculties
def home(request, uname):
    #redirecting faculties to their specific homepage and admin to adminpage  
    temp = User.objects.get(username = request.user.username)
    if temp.username == uname:
        if request.user.is_superuser:
            return render(request,"admin/adminhome.html")
        else:
            if request.user.is_authenticated:
                sub = subject.objects.filter(faculty = uname)
                params = {
                    "subjects" : sub,
                }
                return render(request, "faculty/userhome.html",params)
            else:
                return HttpResponse("error 404: page not found")
    else: 
        return HttpResponse("error")

#manage Question banks
def managequestionbank(request,uname,subcode):
    temp = User.objects.get(username = request.user.username)
    if temp.username == uname:
        if request.method == "POST":
            chno = request.POST['chapterno']
            marks = request.POST['selectmarks']
            diff = request.POST['selectdifficulty']
            question = request.POST['question']
            print(chno,marks,diff,question)
            if len(question) > 5:
                myobj = questionbank(subject_code = subcode, chapterno = chno, marks = marks , difficulty = diff, content = question)
                myobj.save()
            return redirect('managequestionbank',uname,subcode)

        mark1 = questionbank.objects.filter(subject_code = subcode,marks = 1)
        mark2 = questionbank.objects.filter(subject_code = subcode,marks = 2)
        mark5 = questionbank.objects.filter(subject_code = subcode,marks = 5)
        
        params = {
            "subjectcode" : subcode,
            "mark1" : mark1,
            "mark2" : mark2,
            "mark5" : mark5,
        }
        return render(request, "faculty/managequestionbank.html",params)