from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from .models import Task
from datetime import datetime


@login_required
def task_list(request):
    # Update task statuses before rendering the task list
    tasks = Task.objects.filter(user=request.user).order_by("-date", "-start_time")
    for task in tasks:
        task_end_datetime = datetime.combine(task.date, task.end_time)
        if task_end_datetime < datetime.now() and not task.is_completed:
            task.status = "Time Over"
        elif task.proof_of_work and task.admin_approved and not task.is_completed:
            task.is_completed = True
            task.status = "Completed"
        elif not task.proof_of_work and not task.is_completed:
            task.status = "Pending Proof of Work"
        task.save()
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

def update_task_status(request):
    tasks = Task.objects.all()

    for task in tasks:
        # Get the current time and compare it with the task's end time
        task_end_datetime = datetime.combine(task.date, task.end_time)

        # Check if the task time has passed
        if task_end_datetime < datetime.now() and task.is_completed is False:
            task.status = "Times Over"
        
        # Check if the proof of work is uploaded
        elif task.proof_of_work and task.is_completed is False:
            task.status = "Completed"
        
        task.save()

    return JsonResponse({"status": "updated"})
