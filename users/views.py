from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def Register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            pwd = form.password
            form.password = make_password(pwd)

            #sending mail
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.email,]
            subject = 'Welcome to MovRev'
            message = f'Hello {form.username}, Thanks for registering into my application'
            send_mail(subject,message,email_from,recipient_list)

            form.save()
            #return HttpResponse('Regisered successfully')
            return redirect('home')
        else:
            print(form.errors)
            
    context = {'form':form}
    return render(request,'register.html',context)

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect('/home/')
#         else:
#             messages.error(request, 'Invalid user')
#     form = AuthenticationForm()
#     context = {'form':form}
#     return render(request,'login.html',context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('home')