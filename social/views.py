from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def log_out(request):
    logout(request)
    return 