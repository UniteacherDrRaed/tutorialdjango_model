from django.db import models

# Create your models here.

class Uebung(models.Model):
    Frage=models.CharField(max_length=250)
    Antwort=models.CharField(max_length=210)
    
    def __str__(self):
        return f"{self.Frage}: Antwrot: {self.Antwort}"
