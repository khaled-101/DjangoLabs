from django.urls import path
from .views import home , contact ,retriveclassroom

urlpatterns = [
    path("home/", home , name="home"),
    path("home/<str:name>/", home, name='home'),
    path("contact" , contact , name="contact"),
    path("classroom/<str:class_name>/", retriveclassroom, name="classroom_detail")
    
]