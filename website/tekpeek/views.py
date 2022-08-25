from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

# Create your views here.
def tekpeek(request):
    collected_data = models.Data.objects.all()
    news_data = models.News.objects.all()
    html_page = loader.get_template('blog-page.html')
    print(len(news_data))
    print("Database contains: ")
    return HttpResponse(html_page.render({'data': collected_data,'news':news_data}))

def blog_template(request,id):
    collected_data = models.Data.objects.all()
    #collected_data = models.Data.objects.all()
    feed_data=0
    for i in collected_data:
        if i.id == id:
            feed_data=i
            break
    blog_page = loader.get_template('blog-template.html')
    feed_data = {'data':feed_data}
    return HttpResponse(blog_page.render(feed_data))