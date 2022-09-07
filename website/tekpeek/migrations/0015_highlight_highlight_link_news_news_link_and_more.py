# Generated by Django 4.0.6 on 2022-09-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekpeek', '0014_auto_20220829_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='highlight_link',
            field=models.TextField(default='https://www.google.com', max_length=200),
        ),
        migrations.AddField(
            model_name='news',
            name='news_link',
            field=models.TextField(default='https://www.google.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
