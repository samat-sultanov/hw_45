from django.shortcuts import render, get_object_or_404, redirect
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
        return render(request, 'create.html', {"statuses": STATUS_CHOICES})
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        if len(request.POST.get("execution_date")) > 1:
            execution_date = request.POST.get("execution_date")
        else:
            execution_date = None
        new_task = Task.objects.create(title=title, description=description, status=status,
                                       execution_date=execution_date)
        return redirect('task_view', pk=new_task.pk)
