from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from accounts.forms import user_register_form,profile_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_view(request):
    return render(request,'accounts/home.html')

def register_user_view(request):
    if request.method=='POST':
        userform=user_register_form(request.POST)
        p_form=profile_form(request.POST,request.FILES)
        if userform.is_valid() and p_form.is_valid():
            user=userform.save()
            profile=p_form.save(commit=False)
            profile.user=user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        uform=user_register_form()
        pform=profile_form()
    
    return render(request,'accounts/register.html',{'u_form':uform,'p_form':pform})

def login_user_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pword=request.POST.get('password')
        user=authenticate(request,username=uname,password=pword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')
            return render(request, 'accounts/login.html')

    else:
        return render(request,'accounts/login.html')    
    
def logout_view(request):
    logout(request)
    return redirect('login')

