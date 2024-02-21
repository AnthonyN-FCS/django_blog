
from django.shortcuts import render, redirect


def maintenance_home(request):
    return render(request, 'maintenance_log/maintenance-home.html')
