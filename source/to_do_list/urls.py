"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, create_task, task_view, update_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('tasks/add/', create_task, name='task_add'),
    path('task/<int:pk>/update', update_task, name='update_task'),
    path('task/<int:pk>/delete', delete_task, name='delete_task'),
]
