# Generated by Django 4.0.6 on 2022-08-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekpeek', '0007_alter_data_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='blog_date',
            field=models.TextField(max_length=11),
        ),
    ]
