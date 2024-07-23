from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


tasks = ["Cleaning", "Cooking", "Laundry"]

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

@csrf_protect
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))

        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

@csrf_protect
def delete(request, task_index):
    if request.method == "POST":
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
        return redirect("tasks:index")
    return render(request, "tasks/delete.html", {
        "task": tasks[task_index],
        "task_index": task_index
    })