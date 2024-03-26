from django.http import HttpResponse
from django.shortcuts import render


def login_user(request):
    return HttpResponse("Login Page")

def logout_user(request):
    return HttpResponse("Logout Page")