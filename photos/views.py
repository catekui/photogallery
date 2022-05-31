from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Category, Photo


# Create your views here.

def base(request):
    return render(request,'photos/base.html')

def index(request):
    return render(request,'photos/index.html')

def gallery(request):
    category = request.GET.get('category')
    # print('category:', category )
    if category == None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(category__name=category)


    categories = Category.objects.all()
    # photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html' , context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html',{'photo': photo} )


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        # print('data:', data)
        # print('image:', image)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None 

        photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image
            )
        return redirect('gallery')
    context = {'categories': categories}
    return render(request, 'photos/add.html',context) 

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"categories": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})


