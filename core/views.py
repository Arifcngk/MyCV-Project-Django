from django.http import HttpResponse
from django.shortcuts import render
from core.models import *

def index(request):
    about=About.objects.all()
    skill=Skill.objects.all()
    images= Images.objects.filter(name="about")
    imageServices = Images.objects.filter(name="services").first() 

    context={
        'about':about,
        'skill':skill,
        'images':images,
        'imageServices':imageServices,
      

    }
    return render(request,"index.html",context=context)
    


def contact(request):
    return render(request,"contact.html")


