from django.shortcuts import render

from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.order_by("-created_at")
    context = {"tasks": tasks}
    return render(request, 'index.html', context)


def create_task(request):
    if request.method == 'GET':
        return render(request, 'create.html', {"statuses": STATUS_CHOICES})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        if len(request.POST.get("execution_date")) > 1:
            execution_date = request.POST.get("execution_date")
        else:
            execution_date = None
        new_task = Task.objects.create(description=description, status=status, execution_date=execution_date)
        context = {"task": new_task}
        return render(request, 'task_view.html', context)
