from django.shortcuts import render
from .models import Will

def allwills(request):
    wills = Will.objects
    return render(request, 'wills/allwills.html', {'wills':wills})
# Create your views here.
