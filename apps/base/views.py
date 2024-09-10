from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

# def about(request):
#     text = "Мы создаем экосистему для обучения,  работы и творчества IT-специалистов"
#     return HttpResponse(text)

# def index(request):
#     return render(request, 'index.html')

def about(request):
    main_page = "О нас"
    # about = About.objects.latest('id')
    about = About.objects.all()
    return render(request, 'about.html', locals())