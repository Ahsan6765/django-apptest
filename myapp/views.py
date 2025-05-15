from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm

# Home Page View
def home(request):
    return render(request, 'home.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect('login')  # or redirect('home') if you prefer
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
