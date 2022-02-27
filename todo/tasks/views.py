from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.

def index(request):
    # # Use HTTP to print something
    # return HttpResponse('Hello World')
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        # Get the data from the HTML form 
        form = TaskForm(request.POST)

        # Saving the task to the database
        if form.is_valid():
            form.save()

        # Return the same template as a GET method 
        return redirect('/')


    context = {'tasks' : tasks, 'form':form}
    return render(request, 'tasks/list.html', context)