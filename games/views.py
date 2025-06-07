from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def games_home(request):
    return render(request, 'games/games_home.html')
