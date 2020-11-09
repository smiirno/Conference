from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Presenter, Listener
from django.contrib.auth.models import User


def index(request):
    return render(request, 'users/registration.html')

def detail(requests):
    return render(requests, 'users/login.html')
