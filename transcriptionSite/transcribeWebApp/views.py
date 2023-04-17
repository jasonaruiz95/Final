from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "transcribeWebApp/index.html")

def liveTranscribe(request):
    return render(request, "transcribeWebApp/liveTranscribe.html")
