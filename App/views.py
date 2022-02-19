
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render,redirect

from .forms import ResistraionForm,CustomAuthenticationForm
from django.contrib import messages

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import EmailOtp, UserDetail
from .forms import UserDetailForm
import random
from Seller.models import Category

def home(request):
    cat=Category.objects.all()

   
    return render(request,'App/home.html',{'cat':cat})

def Signin(request):
    request.session['VefifyingUser']=request.POST.get('username')
    

   
    if request.method=="POST":
    
        form=CustomAuthenticationForm(request=request,data=request.POST)
        u_name=request.POST.get('username')
        u=User.objects.filter(username=u_name).first()
        
       
        
        
       
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            is_verified=user.userdetail.is_verified
            if is_verified:
                  if user is not None:
                      login(request,user)
                      return HttpResponseRedirect('/')
            else:
                SendingMail(u_name)
                messages.error(request,'You are not verified  user please verify ')
                return HttpResponseRedirect('/Account/Verify/')
               
          
        


    else:
        form=CustomAuthenticationForm()
        

    

    return render(request,'App/login.html',{'form':form})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/Signin/')

def SendingMail(useremail):
    otp=random.randint(1000,9999)
    user=User.objects.filter(username=useremail).first()

    EmailOtp(user=user,otp=str(otp)).save()
    send_mail('Welcome To DjangoEcommerce',f"Your DjangoEccomerce Otp is: {otp}",'djangoecommerce25@gmail.com',[useremail],fail_silently=False)




    


def SignUp(request):
    
    if request.method=='POST':
        fm=ResistraionForm(request.POST)
        username=request.POST.get('username')
        user=User.objects.filter(username=username).first()
        
        if fm.is_valid():
            fm.save()
            username=fm.cleaned_data.get('username')
          
            usr=User.objects.filter(username=username).first()
            if username.isdigit():
                UserDetail(user=usr,mobile=username).save()

                
                

            else:
                UserDetail(user=usr).save()
                usr.email=username
                request.session['VefifyingUser']=username
                usr.save()
                SendingMail(username)
                return HttpResponseRedirect('/Account/Verify')
                


            
            
    else:
        fm=ResistraionForm()
    return render(request,'App/Signup.html',{'form':fm})
def profile(request):
    return render(request,'App/profile.html')

def user_change_form(request):
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)

        if fm.is_valid():
            fm.save()
    fm=PasswordChangeForm(user=request.user)
    return render(request,'App/changepass.html',{'form':fm})

def Myaccount(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/Signin/')
    if request.method=='POST':
        ud_form=UserDetailForm(request.POST,request.FILES,instance=request.user.userdetail)
        if ud_form.is_valid():
            ud_form.save()
    ud_form=UserDetailForm(request.FILES,instance=request.user.userdetail)

    return render(request,'App/Myaccount.html',{'form':ud_form})

def AccountVerify(request):
    try:
        username=request.session['VefifyingUser']
        print('username',username)
        
        usr=User.objects.filter(username=username).first()
        Dbotp=EmailOtp.objects.filter(user=usr).last().otp
     

        if request.method=='POST':
            check=request.POST.get('Otp')
            if check==Dbotp:
               
        
                ud=UserDetail(user=usr)
                ud.is_verified=True
                ud.save()
                messages.error(request,'successfully verified')
                return HttpResponseRedirect('/Signin/')
                
            else:
                messages.error(request,'Plase Enter Correct Otp')
      
            
            
          
    except:
        pass
        
   


    return render(request,'App/Verify.html')




        
            

           

 
   




        


    






   
   

 