from django.shortcuts import render

from django.http import request
# Create your views here.

def home(request):

    return render(request, "index.html")


def login(request):

    return render(request, "pages/login.html")


def register(request):
    return render(request, "pages/register.html")
