from django.shortcuts import render
from django.http import HttpResponse
from .models import Math
# Create your views here.

def mainPage(request):
    maths = Math.objects.all()
    context = {'maths': maths}
    return render(request, 'board/index.html',context)

def index(request):
    return HttpResponse("welcome to my world")

def mp4(request):
    return render(request, 'board/mp4.html')