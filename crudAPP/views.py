from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile
from django.db.models import Q
import os

# Create your views here.
def home(request):
    src= request.GET.get('src')
    if src:
        allProfile = profile.objects.filter(Q( name__icontains=src) | Q( email= src))
    elif src == 'none':
        allProfile = profile.objects.all()
        
    else:
        allProfile = profile.objects.all()
    context ={
       "prof" : allProfile,
       "src" : src
    }
    return render(request,'home.html',context)


def account(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        image = request.FILES.get('image')
        if image:
            if name:
                data = profile.objects.create(name=name, email=email,age=age,gender=gender,phone=phone,address=address,image=image)
                data.save()
                return redirect('home')
            else:
                messages.success(request,f"please fill all fild ! .. ")
                return redirect('home')
            
        else:
            data = profile.objects.create(name=name, email=email,age=age,gender=gender,phone=phone,address=address)
            data.save()
        return redirect('home')
        

    return render(request,'account.html')

def profilePage(request,id):
    prof = profile.objects.get(id=id)
    return render(request,'profileDet.html',locals())



def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def singup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'singup.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')

def DeleteProfile(request,id):
    delete_prof = profile.objects.get(id=id)
    if delete_prof.image != "images/default/user.png":
        os.remove(delete_prof.image.path)
    delete_prof.delete()
    messages.success(request, 'Profile details Deleted...')
    return redirect('home')


def update(request,id):
    upd_prof =profile.objects.get(id=id)
    if request.method=="POST":      
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        image = request.FILES.get('image')

        if upd_prof.image != "images/default/user.png":
            os.remove(upd_prof.image.path)
        upd_prof.image = image
        upd_prof.name = name
        upd_prof.email = email
        upd_prof.age = age
        upd_prof.gender = gender
        upd_prof.phone = phone
        upd_prof.address = address
        upd_prof.save()
        return redirect('home')
    return render(request, 'update.html',locals())