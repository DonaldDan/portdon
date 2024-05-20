from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portdon/index.html')

def about(request):
    return render(request,'portdon/about.html')

def projects(request):
    return render(request,'portdon/projects.html')

def upcoming(request):
    return render(request,'portdon/upcoming.html')

def ongoing(request):
    return render(request,'portdon/ongoing.html')