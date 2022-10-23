from django.shortcuts import render
from django.http import HttpResponse
from .models import PageNumber, VoiceNumber, PageFunctions


# Create your views here.
def index(response, id):
    page_number = PageNumber.objects.get(id=id)
    x = int(id)
    y = x + 1
    return render(response, f"mainsite/{x}.html", {"page_number": page_number, "y": y})


def home(response):
    return render(response, "mainsite/home.html", {})

