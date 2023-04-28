# Generated by Django 4.0.10 on 2023-04-17 09:42

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_rename_chef_meal_chef_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True)),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('body', models.TextField(verbose_name='meal content')),
                ('banner_image', models.ImageField(upload_to='', verbose_name='banner image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ListofWarnings',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True)),
                ('body', models.TextField(verbose_name='warning content')),
                ('banner_image', models.ImageField(upload_to='', verbose_name='banner image')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_warnings', to='meal.meal')),
            ],
            options={
                'verbose_name': 'List of Warning on Meal',
                'verbose_name_plural': 'List of Warnings',
            },
        ),
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(null=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='meals_of_category', to='meal.category', verbose_name='category'),
        ),
    ]
