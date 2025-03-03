from django.views.generic import ListView
from .models import School, Classroom

class SchoolListView(ListView):
    model = School
    template_name = "schools_list.html"  
    context_object_name = "schools"       

class ClassroomListView(ListView):
    model = Classroom
    template_name = "classrooms_list.html"  
    context_object_name = "classrooms"