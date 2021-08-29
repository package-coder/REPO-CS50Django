from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []
 
class TaskDAOForm(forms.Form):
    task = forms.CharField(label="Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def new(request):
    if request.method == 'POST':
        form = TaskDAOForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/new.html", {
                "form": form
            })

    return render(request, "tasks/new.html",{
        "forms": TaskDAOForm()
    })