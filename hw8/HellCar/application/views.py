from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.request import Request


def login_is_required(func):
    """
    A decorator that checks login user. Usage::
        @require_http_methods
        def my_view(request):
            # ...
    """

    @wraps(func)
    def inner(*args, **kwargs):
        is_authenticated = False
        if isinstance(args[0], WSGIRequest):
            is_authenticated = args[0].user.is_authenticated
        else:
            is_authenticated = args[1].user.is_authenticated
        if not is_authenticated:
            return HttpResponseRedirect('/login/')
        return func(*args, **kwargs)

    return inner


@login_is_required
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')
