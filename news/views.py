
from django.shortcuts import render
from .models import loading

def student_details(request):

    allstudents = loading.objects.all()

    print("TOTAL STUDENTS:", allstudents.count())

    for student in allstudents:
        print(
            student.Roll_number,
            student.name,
            student.division
        )

    return render(request, "code.html", {
        "allstudents": allstudents
    })
