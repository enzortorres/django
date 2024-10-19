from django.shortcuts import render

def index(request):
    """Página principal do LearningLog"""
    return render(request, 'learningLogs/index.html')
