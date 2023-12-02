from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainPage),
    path('mp4', views.mp4),
    path('aws', views.aws),
]

