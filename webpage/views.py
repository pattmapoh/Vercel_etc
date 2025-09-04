from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def students_list(request):
    from .models import Students
    students = Students.objects.all()
    return render(request, 'students.html', {'students': students})

def subjects_list(request):
    from .models import Subjects
    subjects = Subjects.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})