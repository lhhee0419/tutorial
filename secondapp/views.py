from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def show(request):
    hospital = Hospital.objects.all()
#    return render(request, 'show.html', {'list':hospital})
    return render(request, 'show.html', {'list':hospital})
