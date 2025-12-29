from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    student = [
       { 'id' : 1, 'name' : 'isha'}
    ]
    return HttpResponse(student)
