from django.shortcuts import render
from django.http import HttpResponseRedirect
from tasks.models import Task


tasks = []
completed = []

def task_view(request) :
    return render(request, "tasks.html", {"tasks" : Task.objects.filter(completed=False, deleted=False)})

def add_task_view(request) :
    task_name = request.GET.get("task")
    Task.objects.create(title=task_name)
    return HttpResponseRedirect("/tasks")

def delete_task_view(request, index) :
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks")

def complete_task_view(request, index) :
    Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/completed_tasks")

def completed_tasks_view(request) :
    return render(request, "completed.html", {"completed" : Task.objects.filter(completed=True, deleted=False)})

def all_tasks_view(request) :
    return render(request, "all_tasks.html", {"all_tasks" : Task.objects.filter(deleted=False)})