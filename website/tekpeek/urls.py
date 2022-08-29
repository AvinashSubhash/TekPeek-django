from django.urls import path
from . import views

urlpatterns = [
    path('',views.tekpeek,name='tekpeek'),
    path('blogs/<int:id>',views.blog_template,name="blog-template")
]