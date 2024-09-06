from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

# def about(request):
#     text = "Мы создаем экосистему для обучения,  работы и творчества IT-специалистов"
#     return HttpResponse(text)

def index(request):
    return render(request, 'index.html')

def about(request):
    text = {
        "title": "О нас",
        "description": "Мы создаем экосистему для обучения,  работы и творчества IT-специалистов",
        "students": ['Эргашев Даниер', 'Умаралие Акназар', 'Абдимиталипов Жанболот ', 'Сайдабаров Азамхожа', 'Идирисов Абдуазим']
    }
    return render(request, 'about.html', text)