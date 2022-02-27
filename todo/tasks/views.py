from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
    # # Use HTTP to print something
    # return HttpResponse('Hello World')
    tasks = Task.objects.all()

    context = {'tasks' : tasks}

    return render(request, 'tasks/list.html', context)