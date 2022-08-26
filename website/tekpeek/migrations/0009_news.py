# Generated by Django 4.0.6 on 2022-08-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekpeek', '0008_alter_data_blog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.TextField(max_length=1000)),
                ('news_title', models.TextField(max_length=300)),
                ('news_short', models.TextField(max_length=300)),
            ],
        ),
    ]