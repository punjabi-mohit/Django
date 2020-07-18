from django.shortcuts import render,redirect
from .forms import Register_Form,Login_form
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def logout_page(request):
    logout(request)
    return redirect("home")


def login_page(request):
    login_pg=Login_form(request.POST or None )
    context={'form':login_pg}
    if login_pg.is_valid():
        un=login_pg.data.get('username')
        pw=login_pg.data.get('pwd')
        user=authenticate(username=un,password=pw)
        if user:
            print(user)
            login(request,user)
            return redirect('home')
    return render(request,'accounts/login1.html',context)



def register_page(request):
    register_form=Register_Form(request.POST or None)
    context={'form':register_form}
    if register_form.is_valid():
        fn=register_form.cleaned_data.get('fname')
        ln=register_form.cleaned_data.get('lname')
        un=register_form.cleaned_data.get('username')
        em=register_form.cleaned_data.get('email')
        pw=register_form.cleaned_data.get('pwd')
        cp=register_form.cleaned_data.get('cpwd')
        user=User.objects.create_user(first_name=fn,last_name=ln,username=un,email=em,password=pw)
        if user:
            context['msg']:'user Created'
        # else:
        #     register_form=Register_Form()
    return render(request,'accounts/register.html',context)