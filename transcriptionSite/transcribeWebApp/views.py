from django.shortcuts import render, redirect
from .models import Transcripts
from .forms import TranscriptForm
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def index(request):
    return render(request, "transcribeWebApp/index.html")

def liveTranscribe(request):
    # form = TranscriptForm(request.POST or None)

    if request.method == 'POST':
        
        transcript = Transcripts(transcript=request.POST.get('transcript'))
        transcript.save()
        # return redirect('transcribeWebApp/transcriptions.html')

    return render(request, "transcribeWebApp/liveTranscribe.html")

def fileTranscriptions(request):
    return render(request, "transcribeWebApp/fileTranscriptions.html")
