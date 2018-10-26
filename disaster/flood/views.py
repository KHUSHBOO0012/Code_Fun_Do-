from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from . import predict

def index(request):
     return render(request, 'flood/index.html')
def prediction(request):
     predict.main(request.POST['regions'])
     return render(request, 'flood/predict.html')
