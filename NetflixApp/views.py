from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def register(request):
#     return render(request, 'accounts/registration_form.html')
