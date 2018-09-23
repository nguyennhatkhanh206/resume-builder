from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, Django!")

def detail(request, resume_id):
    return HttpResponse("You are looking at resume %s" % resume_id)

def result(request, resume_id):
    response = "You are looking at result of resume %s"
    return HttpResponse(response % resume_id)
    