from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user, is_completed=False)
    return render(request, "tasks/task_list.html", {"tasks": tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect("task_list")