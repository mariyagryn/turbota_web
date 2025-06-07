from django.shortcuts import render

def support_home(request):
    # Головна сторінка підтримки
    return render(request, 'support/support_home.html')

