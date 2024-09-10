from django.shortcuts import render
from apps.base.models import About

# Create your views here.
def index(request):
    about = About.objects.latest('id')
    return render(request, 'index.html', locals())