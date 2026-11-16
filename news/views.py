
from django.shortcuts import render
from .models import loading

def student_details(request):

    allstudents = loading.objects.all()

    return render(request, "code.html", {
        "allstudents": allstudents
    })
