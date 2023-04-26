from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


app_name = 'transcribeWebApp'
urlpatterns = [
    path('', views.index, name="index"),
    path('liveTranscribe/', views.liveTranscribe, name='liveTranscribe'),
    path('fileTranscriptions/', views.fileTranscriptions, name='fileTranscriptions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)