# Generated by Django 4.2.7 on 2023-11-27 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComicStrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComicPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('prompt', models.TextField(blank=True, null=True)),
                ('comicstrip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comicstrip')),
            ],
        ),
    ]
