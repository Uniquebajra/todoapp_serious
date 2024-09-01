from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_datetime
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todoapp/task_detail.html', {'task': task})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date_str = request.POST.get('due_date')
        due_date = parse_datetime(due_date_str) if due_date_str else None

        new_task = Task(
            title=title,
            description=description,
            due_date=due_date
        )
        new_task.save()
        return redirect('task_list')  # Redirect to the task list after adding
        
    return render(request, 'todoapp/add_task.html')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        due_date_str = request.POST.get('due_date')
        due_date = parse_datetime(due_date_str) if due_date_str else None

        # Update the task with the new data
        task.title = title
        task.description = description
        task.completed = completed
        task.due_date = due_date
        task.save()

        return redirect('task_detail', pk=task.pk)

    return render(request, 'todoapp/edit_task.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'todoapp/delete_task.html', {'task': task})