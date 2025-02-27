from django.shortcuts import render
from django.http import HttpResponse
def home (request,name = "world"):
    return HttpResponse(f"Hello {name} ")
def contact (request):
    return HttpResponse("this is the cotact page")
def retriveclassroom(request, class_name):
    context = { 
        "title":class_name,
        "description":"this is a class this just a filler to check the funcationality of the if function inside index.html"
    }
    return render(request,"index.html", context)   