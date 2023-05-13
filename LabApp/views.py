from django.shortcuts import render, redirect, get_object_or_404
from .models import Lab, Pc
from .forms import LabForm
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def all_projects(request):
    return render(request, "LabApp/AllProjects.html")

def home(request):
    return render(request, "LabApp/HomePage.html")

@login_required
def list_all_labs(request):
    labs = Lab.objects.all()
    context = {
        "labs":labs,
        "title": "Laboratories List",
    }
    return render(request, "LabApp/LaboratoriesList.html", context)

@login_required
def add_lab(request):
    if request.method == "POST":
        form = LabForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Lab Added Successfully")
            return redirect("list_all_labs")
    else:
        form = LabForm()
    context = {
        "form": form,
        "title": "Add Lab",
        "buttonName": "Add",
    }
    return render(request, "LabApp/Lab_Add_Edit.html", context)

@login_required
def edit_lab(request, lab_id):
    try:
        id_lab = int(lab_id)
        lab = get_object_or_404(Lab, id= id_lab)

        if request.method == "POST":
            form = LabForm(request.POST, instance=lab)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Lab Saved Successfully")
                return redirect("list_all_labs")
        else:
            form = LabForm(instance=lab)
        context = {
            "form": form,
            "title": "Edit Lab",
            "buttonName": "Save",
            "lab": lab,
        }
        return render(request, "LabApp/Lab_Add_Edit.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest()


@login_required
def delete_lab(request, lab_id):
    try:
        id_lab = int(lab_id)
        lab = get_object_or_404(Lab, id= id_lab)
        if request.method == "POST":
            lab.delete()
            messages.add_message(request, messages.SUCCESS, "Lab Deleted Successfully")
            return redirect("list_all_labs")
        else:
            context = {
                "pageTitle":editLab,
                "object":lab,
            }
            return render(request, "LabApp/DeleteConfirmation.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest
