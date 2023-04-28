# Generated by Django 4.0.10 on 2023-03-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='experience',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='university',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
