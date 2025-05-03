from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def view(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def landing_page(request):
    return render(request, 'landing.html')
