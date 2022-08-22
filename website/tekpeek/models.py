from django.db import models
import datetime
# Create your models here.
class Data(models.Model):
    blog_content = models.TextField(max_length=16777215)
    blog_title = models.TextField(max_length=65535)
    blog_short = models.TextField(max_length=255)
    blog_date = models.TextField(max_length=11)
    blog_auth = models.TextField()
    blog_image = models.TextField()