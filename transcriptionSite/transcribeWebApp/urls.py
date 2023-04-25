from . import views
from django.urls import path

app_name = 'transcribeWebApp'
urlpatterns = [
    path('', views.index, name="index"),
    path('liveTranscribe/', views.liveTranscribe, name='liveTranscribe'),
    path('fileTranscriptions/', views.fileTranscriptions, name='fileTranscriptions'),
]
