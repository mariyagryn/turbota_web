from django.shortcuts import redirect
from functools import wraps
from django.shortcuts import render

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('users:login')
            user_groups = set(request.user.groups.values_list('name', flat=True))
            if any(role in user_groups for role in allowed_roles):
                return view_func(request, *args, **kwargs)
            return render(request, '../templates/users/no_access.html')
        return wrapper
    return decorator
