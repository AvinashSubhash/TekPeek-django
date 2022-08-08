from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def homepage(request):
    html_page = loader.get_template('index.html')
    return HttpResponse(html_page.render())