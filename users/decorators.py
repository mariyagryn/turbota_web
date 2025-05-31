from django.shortcuts import redirect
from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            print("DEBUG: User =", request.user)
            print("DEBUG: Authenticated =", request.user.is_authenticated)
            print("DEBUG: Role =", getattr(request.user, 'role', None))
            print("DEBUG: Allowed =", allowed_roles)

            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return render(request, 'users/no_access.html')
        return wrapper
    return decorator
