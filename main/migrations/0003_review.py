# Generated by Django 2.2.4 on 2020-12-19 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_course_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_left', to='main.User')),
                ('course_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.Course')),
            ],
        ),
    ]
