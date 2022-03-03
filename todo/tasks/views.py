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

# pk means primary key
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    # Prefill the form when trying to update it
    form = TaskForm(instance=task)

    if request.method == 'POST':
        # We still need instance=task or else it would create a new todo
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    # Dictionary that stores value of previous form value 
    # Used to render the value to form
    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item' : item}

    if request.method == 'POST':
        # Delete task
        item.delete()
        return redirect("/")

    return render(request, 'tasks/delete.html', context)