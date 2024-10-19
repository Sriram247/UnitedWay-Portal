from django.http import HttpResponse
from django.shortcuts import render
from backendApp.models import *

def index(request):
    project_list = ProjectListNews.objects.all()
    
    context = {
        'projects': project_list,
    }
    
    
    return render(request,"backendApp/index.html",context)



