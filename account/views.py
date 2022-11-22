from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ContactUsForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.contrib.auth import login as auth_login_view
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'account/login.html')


def home(request):
    return render(request, 'account/home.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            form = auth_login_view(request, user)
            return redirect('students')
    form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST) or None
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    else:
        form = ContactUsForm()
        global_var = RequestContext(request)
        global_var.push({'form': form})
    return render(request, 'account/contact.html', {'form': form})