from functools import wraps
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def logout_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request) 
            return HttpResponseRedirect('/')
        return func(request, *args, **kwargs)
    return wrapper