from django.contrib import admin
from .models import PageNumber, VoiceNumber

# Register your models here.
admin.site.register(PageNumber)
admin.site.register(VoiceNumber)