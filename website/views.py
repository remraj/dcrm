from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib.auth import authenticate,login,logout
from django .contrib import messages
from django import forms
from django.forms import SignUpForm,AddRecordForm
from django.models import Record

# Create your views here.
def home(request):
     records= Record.objects.all()
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request,username='username',password='password')
        if user is not None:
            login(request,user)
            messages.success(request,"you have been logged in")
            return redirect('home')
        else:
            messages.success(request,"there was an error in login")
     else:
         return render (request,'home.html',{'records': records})
def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request,"you have been logout...")
    return redirect('home')
     
def register(request):
   
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=forms.cleaned_data('username')
            password=forms.cleaned_data('password1')
            user=authenticate(username=username,password=password )
            login(request,user)
            messages.success(request,"you have been registered sucessfully")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.object.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"you have to been logged in to view that page")
        return redirect('home')
    
def delete_record(request,pk):
        if request.user.is_authenticated:
            delete_it=Record.object.get(id=pk)
            delete_it.delete()
            messages.success(request,"record sucessfully deleted!")
            return redirect('home')
        else:
            messages.success("you must be logged in for deletion")
            return  redirect('home')
        
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"record is saved")
                return redirect('home')          
        return render(request,'add_record.html',{'form': form})
    else:
        messages.success(request,"you have to login for addding records")
        return redirect('home')
        


        
            



  






