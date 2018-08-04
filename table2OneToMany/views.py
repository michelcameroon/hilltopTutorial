from django.shortcuts import render

# Create your views here.


# views.py
from django.views.generic import ListView
from .models import Student

class StudentList(ListView):
    model = Student
    template_name = 'student_list.html'

