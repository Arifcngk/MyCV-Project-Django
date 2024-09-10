from django.http import HttpResponse
from django.shortcuts import render ,redirect ,get_object_or_404
from core.models import *

def index(request):
    about=About.objects.all()
    skill=Skill.objects.all()
    images= Images.objects.filter(name="about")
    imageServices = Images.objects.filter(name="services").first() 
    projects=Projects.objects.all()
    quotes=Quotes.objects.all()

    context={
        'about':about,
        'skill':skill,
        'images':images,
        'imageServices':imageServices,
        'projects':projects,
        'quotes':quotes,
      

    }
    return render(request,"index.html",context=context)
    


def contact(request):
    return render(request,"contact.html")




def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.documant.url)

    
    
 
   

    

