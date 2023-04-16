from . import views
from django.urls import path

app_name = 'transcribeWebApp'
urlpatterns = [
    path('', views.index, name="index"),
]
