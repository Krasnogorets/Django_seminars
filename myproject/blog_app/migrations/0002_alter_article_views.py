# Generated by Django 5.0.1 on 2024-02-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
