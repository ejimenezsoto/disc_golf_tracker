# Generated by Django 2.2.4 on 2020-12-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_courses', to='main.User'),
        ),
    ]
