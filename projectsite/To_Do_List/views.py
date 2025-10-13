from django.shortcuts import render
from django.views.generic.list import ListView
from To_Do_List.models import Task

# Create your views here.

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = 'home.html'
    paginate_by = 5
    
