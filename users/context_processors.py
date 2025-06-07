from django.urls import reverse

def user_dashboard_context(request):
    if not request.user.is_authenticated:
        return {}
    if request.user.is_superuser:
        return {
            'user_dashboard_url': '/admin/',
            'user_dashboard_label': request.user.username
        }
    for group in request.user.groups.all():
        if group.name == 'parent':
            return {
                'user_dashboard_url': reverse('users:parent_dashboard'),
                'user_dashboard_label': request.user.username
            }
        if group.name == 'teacher':
            return {
                'user_dashboard_url': reverse('users:teacher_dashboard'),
                'user_dashboard_label': request.user.username
            }
    return {
        'user_dashboard_url': None,
        'user_dashboard_label': request.user.username
    }

