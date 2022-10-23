from django.db import models

# Create your models here.


class PageNumber(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class VoiceNumber(models.Model):
    page_number = models.ForeignKey(PageNumber, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.number


class PageFunctions:
    id: int
    next: int

class song(models.Model):
    file = models.FileField(upload_to='voice/')

