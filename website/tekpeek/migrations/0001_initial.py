# Generated by Django 4.0.6 on 2022-08-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_content', models.TextField()),
                ('blog_id', models.IntegerField()),
            ],
        ),
    ]
