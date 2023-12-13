from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm
from .models import Task 
from django.http import HttpResponse

def list_task(request):
    print(' Within list task view ')
    try:
        tasks = Task.objects.all()
        print('Fetched task : {}'.format(tasks))
        return render(request,'list_task.html',{'title':'Your tasks','tasks':tasks})
    except Exception as e:
        return HttpResponse(repr(e))


def add_task(request):
    print(' Within add task view ')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form.__dict__)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form':form,'title':'Add Task'})

def delete_task(request,task_id):
    print('Delete view Entered')
    try:
        task = get_object_or_404(Task,pk=task_id)
        print(" Got task: {}".format(task))
    except Exception as e:
        return HttpResponse('<b> No More tasks to delete </b>')
    task.delete()
    return redirect('list_task')

