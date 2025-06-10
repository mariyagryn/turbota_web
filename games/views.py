from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='users:login')
def games_home(request):
    return render(request, 'games/games_home.html')

@login_required(login_url='users:login')
def game1(request):
    # game from
    # https://github.com/VectorStatic/Memory-Matching-Game
    return render(request, 'games/game1.html')

@login_required(login_url='users:login')
def game2(request):
    # game from
    # https://github.com/msalman81/Simon-Game
    return render(request, 'games/game2.html')

@login_required(login_url='users:login')
def game3(request):
    # game from
    # https://github.com/kecav/math-quiz
    return render(request, 'games/game3.html')
