# Generated by Django 2.2.12 on 2022-08-29 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekpeek', '0013_delete_datahandler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]