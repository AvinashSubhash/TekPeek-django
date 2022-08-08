from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
# Create your views here.
def tekpeek(request):
    html_page = loader.get_template('blog-page.html')
    return HttpResponse(html_page.render())