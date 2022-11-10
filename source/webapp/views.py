from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.order_by("-created_at")
    context = {"tasks": tasks}
    return render(request, 'index.html', context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def create_task(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', {'form': form, "statuses": STATUS_CHOICES})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get("description")
            status = request.POST.get("status")
            execution_date = form.cleaned_data.get("execution_date")
            new_task = Task.objects.create(title=title, description=description, status=status,
                                           execution_date=execution_date)
            return redirect('task_view', pk=new_task.pk)
        return render(request, 'create.html', {'form': form, "statuses": STATUS_CHOICES})


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'execution_date': task.execution_date
        })
        return render(request, 'update.html', {'form': form, "statuses": STATUS_CHOICES})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.execution_date = form.cleaned_data.get('execution_date')
            task.status = request.POST.get("status")
            task.save()
            return redirect('task_view', pk=task.pk)
        return render(request, 'update.html', {'form': form, "statuses": STATUS_CHOICES})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')
