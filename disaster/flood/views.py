from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
     return render(request, 'flood/index.html')

# Create your views here.
