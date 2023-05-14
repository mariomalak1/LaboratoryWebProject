from django.shortcuts import render, redirect, get_object_or_404
from .models import Lab, Pc, Report
from .forms import LabForm, ReportForm
from django.http import HttpResponseBadRequest
from django.contrib import messages
# Create your views here.

def all_projects(request):
    return render(request, "LabApp/AllProjects.html")

def home(request):
    return render(request, "LabApp/HomePage.html")

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
                "pageTitle":"editLab",
                "object":lab,
            }
            return render(request, "LabApp/DeleteConfirmation.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest

def list_all_reports(request):
    reports = Report.objects.all()
    context = {
        "reports": reports,
    }
    return render(request, "LabApp/ListOfReports.html", context)

def add_report(request, lab_id = None):
    id_lab = 0
    lab = None
    if lab_id:
        id_lab = int(lab_id)
        lab = get_object_or_404(Lab, id = id_lab)
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Report Added Successfully")
            return redirect("list_all_reports")
    else:
        form = ReportForm(lab = lab)
        # if id_lab != 0:
            # form()

    context = {
        "form": form,
        "title": "Add Lab",
        "buttonName": "Add",
    }
    return render(request, "LabApp/ReportProblem.html", context)
    # except:
    #     return HttpResponseBadRequest()

def edit_report(request):
    pass

def delete_report(request, report_id):
    try:
        id_report = int(report_id)
        report = get_object_or_404(Report, id=id_report)
        if request.method == "POST":
            report.delete()
            messages.add_message(request, messages.SUCCESS, "Report Deleted Successfully")
            return redirect("list_all_reports")
        else:
            context = {
                "pageTitle": "editReport",
                "object": report,
            }
            return render(request, "LabApp/DeleteConfirmation.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest