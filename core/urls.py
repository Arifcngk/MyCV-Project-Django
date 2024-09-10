from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 
from .views import redirect_urls

urlpatterns = [
    path("",views.index,name="index"),
    path("contact/",views.contact,name="contact"),
    path("<slug>/",redirect_urls,name="redirect_urls"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

