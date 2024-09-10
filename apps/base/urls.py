from django.urls import path

from apps.base.views import about

urlpatterns = [
    # path('', index, name="index"),
    path('about/', about, name="about"),
]