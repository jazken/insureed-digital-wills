from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def homepage(request):
    return render(request, 'home.html')
