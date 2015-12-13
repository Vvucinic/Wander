from django.shortcuts import render
from django.http import HttpResponse

def add_user_page(request):
    return HttpResponse("Hello, McSwaggins!")

# Create your views here.
