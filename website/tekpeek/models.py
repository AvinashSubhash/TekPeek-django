from django.db import models

# Create your models here.
class Data(models.Model):
    blog_content = models.TextField(max_length=16777215)
    blog_id = models.IntegerField()