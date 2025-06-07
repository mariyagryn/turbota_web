from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='users:login')
def feedback_home(request):
    return render(request, 'feedback/feedback_home.html')

