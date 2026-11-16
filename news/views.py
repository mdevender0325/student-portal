
from django.shortcuts import render
from .models import loading

def student_details(request):

    allstudents = []
    division = "E"
    roll_numbers = ""

    if request.method == "POST":

        division = request.POST.get("division")
        roll_numbers = request.POST.get("roll_numbers", "")

        rolls = roll_numbers.replace(",", " ").split()

        allstudents = loading.objects.filter(
            division=division,
            Roll_number__in=rolls
        )

    return render(request, "code.html", {
        "allstudents": allstudents,
        "selected_division": division,
        "entered_roll_numbers": roll_numbers
    })
