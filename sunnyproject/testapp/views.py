from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exams_view(request):
    return HttpResponse('<h1>Exam View </h1>')
def attendace_view(request):
    return HttpResponse('<h1>Attendance view</h1>')
def fees_view(request):
    return HttpResponse('<h1>Fees view</h1>')