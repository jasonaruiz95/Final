from django.db import models

# Create your models here.

class Transcripts(models.Model):

    def __str__(self):
        return (self.transcript)
    
    transcript = models.CharField(max_length=1000)

