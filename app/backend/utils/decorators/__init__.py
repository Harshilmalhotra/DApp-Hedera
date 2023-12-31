# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from functools import wraps

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect, reverse
from django.conf import settings
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import get_user_model


# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_otp import devices_for_user


User = get_user_model()

def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

def ajax_required(f):
    """
    AJAX request required decorator
    use it in your views:

    @ajax_required
    def my_view(request):
        ....

    """
    def wrap(request, *args, **kwargs):
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponseBadRequest('Invalid request')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
 

def login_forbidden(function):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting
    to the homepage if necessary.
    """
    @wraps(function)
    def wrap(request, *args, **kwargs):
        u = request.user
        if u.is_authenticated:
            return redirect(reverse(settings.LOGIN_REDIRECT_URL))
        return function(request, *args, **kwargs)
 
    return wrap