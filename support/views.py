from django.shortcuts import render, redirect
from .models import Need
from .forms import VolunteerForm
from django.contrib import messages

def support_home(request):
    needs = Need.objects.all()
    return render(request, 'support/support_home.html', {'needs': needs})

def volunteer_form(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Дякуємо за вашу заявку! Ми звʼяжемося з вами найближчим часом.')
            return redirect('support:volunteer_form')
    else:
        form = VolunteerForm()
    return render(request, 'support/volunteer_form.html', {'form': form})
