from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='users:login')
def schedule_home(request):
    return render(request, 'schedule/schedule_home.html')

