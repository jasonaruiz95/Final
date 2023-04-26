from django.shortcuts import render, redirect
from .models import Transcripts
from .forms import TranscriptForm, UploadFileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import speech_recognition as sr
from os import path
from pydub import AudioSegment
from django.core.files.storage import FileSystemStorage

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
    if request.method == "POST" and 'audiofile' in request.FILES:
        print("Entered post method handler")
        request_file = request.FILES['audiofile']
        fs = FileSystemStorage()
        filename = fs.save(request_file.name, request_file)

        fileurl = fs.url(filename)
        handle_uploaded_file(fileurl, filename)

        return render(request, 'transcribeWebApp/fileTranscriptions.html', {
            'fileurl': fileurl})
                        

        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
            # handle_uploaded_file(request.FILES["audiofile"])
        #     return HttpResponseRedirect("transcribeWebApp/index.html")
    else:
        # form = UploadFileForm()
        return render(request, "transcribeWebApp/fileTranscriptions.html")

    return render(request, "transcribeWebApp/fileTranscriptions.html")


def handle_uploaded_file(fileurl, filename):
    # convert mp3 file to wav                                                       
    sound = AudioSegment.from_mp3(fileurl)
    filename = filename + ".wav"
    sound.export(filename, format="wav")


    # transcribe audio file                                                         
    AUDIO_FILE = filename

    # use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file                  

            print("Transcription: " + r.recognize_google(audio))