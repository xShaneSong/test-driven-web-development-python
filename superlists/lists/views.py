from django.shortcuts import render

# Create your views here.
def home_page():
    retun HttpResponse('<html><title>To-Do lists</title></html>')
