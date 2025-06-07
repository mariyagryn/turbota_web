from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render
from .decorators import role_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import get_user_model

def logout_view(request):
    logout(request)
    return redirect('login')
@role_required(['parent'])
def parent_dashboard(request):
    return render(request, '../templates/users/parent_dashboard.html')

@role_required(['teacher'])
def teacher_dashboard(request):
    return render(request, '../templates/users/teacher_dashboard.html')


def custom_login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')

        username = request.POST.get('username')
        password = request.POST.get('password')

        if role == 'guest':
            try:
                guest_user = CustomUser.objects.get(username='guest_user')
                login(request, guest_user)
                return redirect('guest_dashboard')
            except CustomUser.DoesNotExist:
                return render(request, '../templates/users/login.html', {
                    'error': 'Гостьовий користувач не знайдений'
                })

        user = authenticate(request, username=username, password=password)
        print("AUTH RESULT:", user)

        if user is not None and user.role == role:
            print("Успішний вхід:", user.username, user.role)
            login(request, user)
            if role == 'parent':
                return redirect('parent_dashboard')
            elif role == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return render(request, '../templates/users/login.html', {
                    'error': 'Невірний логін або роль'
            })
            print("Невдалий вхід:", username, password, role)

    return render(request, '../templates/users/login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, '../templates/users/register.html', {'form': form})
