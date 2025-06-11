from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ScheduleFile
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from users.decorators import role_required
from django.utils.decorators import method_decorator


@login_required(login_url='users:login')
def schedule_home(request):
    schedule_file = ScheduleFile.objects.order_by('-id').first()
    can_edit = request.user.is_authenticated and hasattr(request.user, 'is_teacher') and request.user.is_teacher()
    context = {
        'schedule_file': schedule_file,
        'can_edit': can_edit,
    }
    return render(request, 'schedule/schedule_home.html', context)


@method_decorator(role_required(['teacher']), name='dispatch')
class ScheduleFileUpdateView(UpdateView):
    model = ScheduleFile
    fields = ['title', 'file']
    template_name = 'schedule/schedule_form.html'
    success_url = reverse_lazy('schedule:schedule_home')
