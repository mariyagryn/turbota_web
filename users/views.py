from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from .decorators import role_required
from .forms import CustomUserCreationForm


def logout_view(request):
    logout(request)
    return redirect('users:login')

@role_required(['parent'])
def parent_dashboard(request):
    return render(request, '../templates/users/parent_dashboard.html')

@role_required(['teacher'])
def teacher_dashboard(request):
    return render(request, '../templates/users/teacher_dashboard.html')


def custom_login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            if user.groups.filter(name='parent').exists():
                return redirect('users:parent_dashboard')
            elif user.groups.filter(name='teacher').exists():
                return redirect('users:teacher_dashboard')
            else:
                error = 'Ваша група не підтримується.'
        else:
            error = 'Неправильний логін або пароль.'
    return render(request, '../templates/users/login.html', {'error': error})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, '../templates/users/register.html', {'form': form})
