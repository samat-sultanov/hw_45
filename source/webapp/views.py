from django.shortcuts import render

from webapp.models import Task


def index_view(request):
    tasks = Task.objects.order_by("-created_at")
    context = {"tasks": tasks}
    return render(request, 'index.html', context)
