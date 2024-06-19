# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')# Redirect to your home page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
# views.py
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('index')  # Redirect to your home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
# views.py
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')  # Redirect to your home page after logout
