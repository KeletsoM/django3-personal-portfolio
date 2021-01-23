from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    return render(request, 'portfolio/index.html')

def data_science(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/data.html', {'projects': projects})
