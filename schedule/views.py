from django.shortcuts import render

def schedule_home(request):
    # Головна сторінка розкладу занять
    return render(request, 'schedule/schedule_home.html')

