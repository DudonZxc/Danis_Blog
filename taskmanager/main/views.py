from django.shortcuts import render
from django.http import  HttpResponse


def index(request):
    return render (request, 'main/index.html')
    return render (request, 'main/contact.html')
    return render (request, 'main/about-us.html')