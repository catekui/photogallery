from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category, Photo


# Create your views here.

def base(request):
    return render(request,'photos/base.html')

def index(request):
    return render(request,'photos/index.html')

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()


    context = {'categories': categories, 'photos': photos}
    return render(request,'photos/gallery.html', context)

def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html', {'photo': photo})



def addPhoto(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request,'photos/add.html')



