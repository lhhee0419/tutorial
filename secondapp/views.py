from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def hospital(request):
    sample = Hospital.objects.all()
    return render(request, 'hospital.html', {'list':sample})
