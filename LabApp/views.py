from django.shortcuts import render, redirect, get_object_or_404
from .models import Lab, Pc, Report
from .forms import LabForm, ReportForm, AddPC_Form
from django.http import HttpResponseBadRequest
from django.contrib import messages
# Create your views here.

def all_projects(request):
    return render(request, "LabApp/AllProjects.html")

def home(request):
    return render(request, "LabApp/HomePage.html", {"title":"Home"})

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
                "lab":lab,
                "title":"Delete Lab Confrimation"
            }
            return render(request, "LabApp/DeleteConfirmation.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest

def list_all_reports(request):
    reports = Report.objects.all()
    context = {
        "reports": reports,
        "title": "List All Reports"
    }
    return render(request, "LabApp/ListOfReports.html", context)

def add_report(request, lab_id = None):
    try:
        lab = None
        if lab_id:
            id_lab = int(lab_id)
            lab = get_object_or_404(Lab, id = id_lab)
        if request.method == "POST":
            form = ReportForm(request.POST, lab = lab)
            if form.is_valid():
                ## send alb to form save, as disable data doesn't send to server backend
                form.save(lab = lab)
                messages.add_message(request, messages.SUCCESS, "Report Added Successfully")
                return redirect("list_all_reports")
        else:
            form = ReportForm(lab = lab)
        context = {
            "form": form,
            "title": "Add Lab",
            "buttonName": "Add",
        }
        return render(request, "LabApp/ReportProblem.html", context)
    except:
        return HttpResponseBadRequest()

def edit_report(request, report_id):
    try:
        id_report = int(report_id)
        report = get_object_or_404(Report, id=id_report)

        if request.method == "POST":
            form = ReportForm(request.POST, instance=report, lab=report.lab)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Report Saved Successfully")
                return redirect("list_all_reports")
        else:
            form = ReportForm(instance=report, lab=report.lab)
        form.fields["date"].initial = report.date
        context = {
            "form": form,
            "title": "Edit Report",
            "buttonName": "Save",
            "report": report,
        }
        return render(request, "LabApp/ReportProblem.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest()

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
                "report": report,
                "title": "Delete Report Confrimation"
            }
            return render(request, "LabApp/DeleteConfirmation.html", context)
    except:
        # if he enters id with id as string not number
        return HttpResponseBadRequest

def add_pc(request):
    if request.method == "POST":
        form = AddPC_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        elif form.errors.as_data()["__all__"]:
            messages.add_message(request, messages.WARNING, "This PC ID In This Lab Is Already Exist")
    else:
        form = AddPC_Form()
    context = {
        "form":form
    }

    return render(request, "LabApp/AddPc.html", context)
