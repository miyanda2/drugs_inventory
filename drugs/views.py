from django.shortcuts import render
from .models import Drug



def home(request):
    drugs = Drug.objects.all()
    return render(request, 'index.html', {'drugs':drugs})

# Create your views here.
