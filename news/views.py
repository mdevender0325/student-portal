from django.shortcuts import render
from .models import loading

def student_details(request):
    teachers = loading.objects.all()
    return render(request, 'code.html',{"allstudents":teachers})
