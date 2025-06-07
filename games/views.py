from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='users:login')
def games_home(request):
    return render(request, 'games/games_home.html')
