from django import forms
from .models import Transcripts



class TranscriptForm(forms.ModelForm):
    class Meta:
        model = Transcripts
        fields = ['transcript']

