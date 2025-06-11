from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


@login_required(login_url='users:login')
def feedback_home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Повідомлення від {name}'
            body = f"Імʼя: {name}\nEmail: {email}\n\n{message}"
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [getattr(settings, 'CONTACT_EMAIL', settings.DEFAULT_FROM_EMAIL)],
                fail_silently=False,
            )
            messages.success(request, 'Дякуємо за звернення!')
            form = ContactForm()  # Очищаємо форму після успіху
    else:
        form = ContactForm()
    return render(request, 'feedback/feedback_home.html', {'form': form})
