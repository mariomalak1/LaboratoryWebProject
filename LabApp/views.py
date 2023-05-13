from django.shortcuts import render, redirect, get_object_or_404
from .models import Lab, Pc
from .forms import LabForm
from django.http import HttpResponseBadRequest
# Create your views here.

def list_all_labs(request):
    labs = Lab.objects.all()
    context = {
        "labs":labs,
        "title": "Laboratories List",
    }
    return render(request, "LabApp/LaboratoriesList.html", context)

def add_lab(request):
    if request.method == "POST":
        form = LabForm(request.POST)
        if form.is_valid():
            PCs_no = form.cleaned_data.get("PCsNumber")
            form.save()
            for _ in PCs_no:
                PC.objects.create(lab= form.cleaned_data.get("name"), status= "Active")
            return redirect("list_all_labs")
    else:
        form = LabForm()
    # print(form["status"])
    context = {
        "form": form,
        "title": "Add Lab",
    }
    return render(request, "LabApp/AddLaboratory.html", context)


def edit_lab(request, lab_id):
    try:
        id_lab = int(lab_id)
        lab = get_object_or_404(Lab, id= id_lab)

        if request.method == "POST":
            form = LabForm()
            if form.is_valid():
                form.save()
                return redirect("list_all_labs")
        else:
            form = LabForm(instance=lab)
        context = {
            "form": form,
            "title": "Edit Lab",
        }
        return render(request, "LabApp/EditLaboratory.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest


def delete_lab(request, lab_id):
    try:
        id_lab = int(lab_id)
        lab = get_object_or_404(Lab, id= id_lab)

    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest