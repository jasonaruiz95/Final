from django import forms
from .models import Transcripts



class TranscriptForm(forms.ModelForm):
    class Meta:
        model = Transcripts
        fields = ['transcript']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()