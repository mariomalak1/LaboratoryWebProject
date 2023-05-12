from django.shortcuts import render
from .models import Lab
# Create your views here.

def list_all_labs(request):
    labs = Lab.objects.all()
    context = {
        "labs":labs
    }
    return render(request, "LabApp/LaboratoriesList.html", context)