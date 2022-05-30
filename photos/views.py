from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.

def base(request):
    return render(request,'photos/base.html')

def index(request):
    return render(request,'photos/index.html')

def gallery(request):
    return render(request,'photos/gallery.html')

def viewPhoto(request, pk):
    return render(request,'photos/photo.html')


def addPhoto(request):
    return render(request,'photos/add.html')



