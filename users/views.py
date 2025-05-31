from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render
def parent_dashboard(request):
    return render(request, 'users/parent_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'users/teacher_dashboard.html')

def guest_dashboard(request):
    return render(request, 'users/guest_dashboard.html')
def custom_login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'guest':
            return redirect('guest_dashboard')

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.role == role:
            login(request, user)
            if role == 'parent':
                return redirect('parent_dashboard')
            elif role == 'teacher':
                return redirect('teacher_dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Невірний логін або роль'})
    return render(request, 'users/login.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
