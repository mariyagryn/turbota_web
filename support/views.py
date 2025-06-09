from django.shortcuts import render
from .models import Need

def support_home(request):
    needs = Need.objects.all()
    return render(request, 'support/support_home.html', {'needs': needs})
