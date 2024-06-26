# Generated by Django 4.1.5 on 2024-06-05 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.CharField(choices=[('B', 'Bachelor'), ('M', 'Master'), ('P', 'PhD')], max_length=1)),
                ('description', models.TextField()),
                ('curriculum', models.TextField()),
                ('application_deadline', models.DateField()),
                ('apply_link', models.URLField()),
                ('view_count', models.IntegerField(default=0)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_degrees', to=settings.AUTH_USER_MODEL)),
                ('save', models.ManyToManyField(blank=True, related_name='saved_degrees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DegreeView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_date', models.DateTimeField(auto_now_add=True)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degree_views', to='educations.degree')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='degree',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degrees', to='educations.school'),
        ),
    ]
